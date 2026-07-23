"""Ejecutor local y síncrono de agentes."""

from __future__ import annotations

from time import monotonic
from typing import Any

from pydantic import ValidationError

from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.context import (
    AgentContext,
    generate_audit_id,
    generate_event_id,
    generate_execution_id,
    utc_now,
)
from editorial_ia.core.contracts import AgentInput, AgentOutput, AuditRecord, ValidationIssue
from editorial_ia.core.errors import (
    AgentNotFoundError,
    EscalationRequiredError,
    InvalidInputError,
    InvalidOutputError,
    LogicalTimeoutError,
)
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.result import AgentResult, AgentResultStatus
from editorial_ia.core.validation import classify_exception, error_issues


class AgentRunner:
    def __init__(
        self,
        registry: AgentRegistry,
        audit_logger: AuditLogger,
        *,
        max_retries: int = 3,
        timeout_seconds: float = 30.0,
    ) -> None:
        if max_retries < 0 or max_retries > 3:
            raise ValueError("max_retries debe estar entre 0 y 3.")
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds debe ser positivo.")
        self.registry = registry
        self.audit_logger = audit_logger
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds

    def run(
        self,
        *,
        agent_id: str,
        project_id: str,
        payload: dict[str, Any],
        metadata: dict[str, Any] | None = None,
        max_retries: int | None = None,
        timeout_seconds: float | None = None,
    ) -> AgentResult:
        retries = self.max_retries if max_retries is None else max_retries
        timeout = self.timeout_seconds if timeout_seconds is None else timeout_seconds
        if retries < 0 or retries > 3:
            raise ValueError("max_retries debe estar entre 0 y 3.")
        if timeout <= 0:
            raise ValueError("timeout_seconds debe ser positivo.")

        event_id = generate_event_id()
        execution_id = generate_execution_id()
        audit_id = generate_audit_id()
        started_at = utc_now()
        raw_input = {
            "project_id": project_id,
            "event_id": event_id,
            "payload": payload,
            "metadata": metadata or {},
        }

        try:
            agent_input = AgentInput.model_validate(raw_input)
        except ValidationError as exc:
            issue = classify_exception(exc)
            return self._finalize(
                agent_id=agent_id,
                agent_version="UNKNOWN",
                project_id=project_id,
                event_id=event_id,
                execution_id=execution_id,
                audit_id=audit_id,
                started_at=started_at,
                status=AgentResultStatus.REJECTED,
                output=None,
                warnings=(),
                errors=(issue,),
                evidence=(),
                next_action="Corregir el contrato de entrada.",
                retryable=False,
                attempt_count=0,
                raw_input=raw_input,
            )

        try:
            agent = self.registry.get(agent_id)
        except AgentNotFoundError as exc:
            issue = classify_exception(exc)
            return self._finalize(
                agent_id=agent_id,
                agent_version="UNKNOWN",
                project_id=project_id,
                event_id=event_id,
                execution_id=execution_id,
                audit_id=audit_id,
                started_at=started_at,
                status=AgentResultStatus.FAILED,
                output=None,
                warnings=(),
                errors=(issue,),
                evidence=(),
                next_action="Registrar explícitamente un agente válido.",
                retryable=False,
                attempt_count=0,
                raw_input=raw_input,
            )

        input_issues = agent.validate_input(agent_input)
        input_errors = error_issues(input_issues)
        if input_errors:
            return self._finalize(
                agent_id=agent.agent_id,
                agent_version=agent.version,
                project_id=project_id,
                event_id=event_id,
                execution_id=execution_id,
                audit_id=audit_id,
                started_at=started_at,
                status=AgentResultStatus.REJECTED,
                output=None,
                warnings=tuple(issue for issue in input_issues if issue not in input_errors),
                errors=input_errors,
                evidence=(),
                next_action="Corregir la entrada antes de reintentar.",
                retryable=False,
                attempt_count=0,
                raw_input=raw_input,
            )

        last_issue: ValidationIssue | None = None
        for attempt in range(1, retries + 2):
            context = AgentContext(
                project_id=project_id,
                execution_id=execution_id,
                event_id=event_id,
                agent_id=agent.agent_id,
                agent_version=agent.version,
                started_at=started_at,
                attempt=attempt,
                timeout_seconds=timeout,
                metadata=metadata or {},
            )
            clock_started = monotonic()
            try:
                output = agent.execute(context, agent_input)
                if not isinstance(output, AgentOutput):
                    raise InvalidOutputError("El agente no devolvió AgentOutput.")
                elapsed = monotonic() - clock_started
                if elapsed > timeout:
                    raise LogicalTimeoutError(
                        f"La ejecución superó el timeout lógico de {timeout} segundos."
                    )
                output_issues = agent.validate_output(output)
                output_errors = error_issues(output_issues)
                if output_errors:
                    raise InvalidOutputError(
                        "; ".join(issue.message for issue in output_errors)
                    )
                return self._finalize(
                    agent_id=agent.agent_id,
                    agent_version=agent.version,
                    project_id=project_id,
                    event_id=event_id,
                    execution_id=execution_id,
                    audit_id=audit_id,
                    started_at=started_at,
                    status=AgentResultStatus.SUCCESS,
                    output=output,
                    warnings=output_issues,
                    errors=(),
                    evidence=output.evidence,
                    next_action="Revisar la salida estructurada.",
                    retryable=False,
                    attempt_count=attempt,
                    raw_input=raw_input,
                )
            except EscalationRequiredError as exc:
                last_issue = classify_exception(exc)
                return self._finalize(
                    agent_id=agent.agent_id,
                    agent_version=agent.version,
                    project_id=project_id,
                    event_id=event_id,
                    execution_id=execution_id,
                    audit_id=audit_id,
                    started_at=started_at,
                    status=AgentResultStatus.ESCALATED,
                    output=None,
                    warnings=(),
                    errors=(last_issue,),
                    evidence=(),
                    next_action="Solicitar resolución humana.",
                    retryable=False,
                    attempt_count=attempt,
                    raw_input=raw_input,
                )
            except Exception as exc:  # noqa: BLE001 - se estructura y audita
                last_issue = classify_exception(exc)
                if attempt <= retries:
                    continue

        if last_issue is None:
            last_issue = classify_exception(InvalidInputError("Fallo sin detalle."))
        return self._finalize(
            agent_id=agent.agent_id,
            agent_version=agent.version,
            project_id=project_id,
            event_id=event_id,
            execution_id=execution_id,
            audit_id=audit_id,
            started_at=started_at,
            status=AgentResultStatus.FAILED,
            output=None,
            warnings=(),
            errors=(last_issue,),
            evidence=(),
            next_action="Revisar el fallo registrado antes de una nueva ejecución.",
            retryable=False,
            attempt_count=retries + 1,
            raw_input=raw_input,
        )

    def _finalize(
        self,
        *,
        agent_id: str,
        agent_version: str,
        project_id: str,
        event_id: str,
        execution_id: str,
        audit_id: str,
        started_at: Any,
        status: AgentResultStatus,
        output: AgentOutput | None,
        warnings: tuple[ValidationIssue, ...],
        errors: tuple[ValidationIssue, ...],
        evidence: tuple[str, ...],
        next_action: str | None,
        retryable: bool,
        attempt_count: int,
        raw_input: dict[str, Any],
    ) -> AgentResult:
        finished_at = utc_now()
        result = AgentResult(
            agent_id=agent_id,
            project_id=project_id,
            execution_id=execution_id,
            event_id=event_id,
            agent_version=agent_version,
            status=status,
            started_at=started_at,
            finished_at=finished_at,
            output=output,
            warnings=warnings,
            errors=errors,
            evidence=evidence,
            next_recommended_action=next_action,
            retryable=retryable,
            attempt_count=attempt_count,
            audit_reference=audit_id,
        )
        audit_record = AuditRecord(
            audit_id=audit_id,
            execution_id=execution_id,
            event_id=event_id,
            project_id=project_id,
            agent_id=agent_id,
            agent_version=agent_version,
            status=status.value,
            started_at=started_at,
            finished_at=finished_at,
            attempt_count=attempt_count,
            input=raw_input,
            output=output.model_dump(mode="json") if output is not None else None,
            warnings=tuple(issue.model_dump(mode="json") for issue in warnings),
            errors=tuple(issue.model_dump(mode="json") for issue in errors),
            evidence=evidence,
            next_recommended_action=next_action,
            retryable=retryable,
        )
        self.audit_logger.persist(audit_record)
        return result
