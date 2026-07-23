from __future__ import annotations

from editorial_ia.agents import EchoTestAgent
from editorial_ia.core.agent import BaseAgent
from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.context import AgentContext
from editorial_ia.core.contracts import (
    AgentAvailability,
    AgentInput,
    AgentLayer,
    AgentMetadata,
    AgentOutput,
)
from editorial_ia.core.errors import EscalationRequiredError
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.result import AgentResultStatus
from editorial_ia.core.runner import AgentRunner


class FailingAgent(BaseAgent):
    def __init__(self) -> None:
        self.calls = 0

    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="TEST-FAIL-001",
            name="Fallo de prueba",
            version="1.0.0",
            layer=AgentLayer.TEST,
            description="Doble de prueba que siempre falla.",
            availability=AgentAvailability.TEST_ONLY,
        )

    def execute(self, context: AgentContext, agent_input: AgentInput) -> AgentOutput:
        self.calls += 1
        raise RuntimeError("fallo controlado")


class EscalatingAgent(FailingAgent):
    @property
    def metadata(self) -> AgentMetadata:
        return super().metadata.model_copy(
            update={"agent_id": "TEST-ESCALATE-001", "name": "Escalado de prueba"}
        )

    def execute(self, context: AgentContext, agent_input: AgentInput) -> AgentOutput:
        self.calls += 1
        raise EscalationRequiredError("requiere humano")


class InvalidOutputAgent(FailingAgent):
    @property
    def metadata(self) -> AgentMetadata:
        return super().metadata.model_copy(
            update={"agent_id": "TEST-OUTPUT-001", "name": "Salida inválida"}
        )

    def execute(self, context: AgentContext, agent_input: AgentInput) -> AgentOutput:
        self.calls += 1
        return AgentOutput(data={"text": "abc", "character_count": 1})

    def validate_output(self, output: AgentOutput):
        return EchoTestAgent().validate_output(output)


def test_runner_success(runner: AgentRunner, audit_logger: AuditLogger) -> None:
    result = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": "Prueba"},
    )
    assert result.status == AgentResultStatus.SUCCESS
    assert result.output.data["text"] == "Prueba"
    assert result.output.data["character_count"] == 6
    assert result.attempt_count == 1
    assert result.audit_reference.startswith("AUD-")
    assert len(audit_logger.read(execution_id=result.execution_id)) == 1


def test_runner_rejects_empty_input(runner: AgentRunner, audit_logger: AuditLogger) -> None:
    result = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": ""},
    )
    assert result.status == AgentResultStatus.REJECTED
    assert result.attempt_count == 0
    assert result.errors[0].code == "TEXT_EMPTY"
    assert len(audit_logger.read()) == 1


def test_runner_reports_missing_agent(runner: AgentRunner) -> None:
    result = runner.run(
        agent_id="NO-EXISTE",
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert result.status == AgentResultStatus.FAILED
    assert result.errors[0].code == "AGENT_NOT_FOUND"


def test_three_retries_then_structured_failure(tmp_path) -> None:
    registry = AgentRegistry()
    agent = FailingAgent()
    registry.register(agent)
    logger = AuditLogger(tmp_path / "audit")
    runner = AgentRunner(registry, logger, max_retries=3)

    result = runner.run(
        agent_id=agent.agent_id,
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert agent.calls == 4
    assert result.attempt_count == 4
    assert result.status == AgentResultStatus.FAILED
    assert result.errors[0].code == "UNHANDLED_EXECUTION_ERROR"
    assert len(logger.read()) == 1


def test_invalid_output_is_retried_and_classified(tmp_path) -> None:
    registry = AgentRegistry()
    agent = InvalidOutputAgent()
    registry.register(agent)
    result = AgentRunner(
        registry,
        AuditLogger(tmp_path / "audit"),
        max_retries=1,
    ).run(
        agent_id=agent.agent_id,
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert agent.calls == 2
    assert result.status == AgentResultStatus.FAILED
    assert result.errors[0].code == "INVALID_OUTPUT"


def test_escalation_is_not_retried(tmp_path) -> None:
    registry = AgentRegistry()
    agent = EscalatingAgent()
    registry.register(agent)
    result = AgentRunner(registry, AuditLogger(tmp_path / "audit")).run(
        agent_id=agent.agent_id,
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert agent.calls == 1
    assert result.status == AgentResultStatus.ESCALATED
    assert result.errors[0].code == "ESCALATION_REQUIRED"


def test_logical_timeout_becomes_structured_failure(tmp_path, monkeypatch) -> None:
    registry = AgentRegistry()
    registry.register(EchoTestAgent())
    ticks = iter((0.0, 2.0))
    monkeypatch.setattr("editorial_ia.core.runner.monotonic", lambda: next(ticks))
    result = AgentRunner(
        registry,
        AuditLogger(tmp_path / "audit"),
        max_retries=0,
        timeout_seconds=1,
    ).run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert result.status == AgentResultStatus.FAILED
    assert result.errors[0].code == "LOGICAL_TIMEOUT"


def test_runner_configuration_limits(registry, audit_logger) -> None:
    for retries in (-1, 4):
        try:
            AgentRunner(registry, audit_logger, max_retries=retries)
        except ValueError as exc:
            assert "max_retries" in str(exc)
        else:
            raise AssertionError("Debió rechazar max_retries")
