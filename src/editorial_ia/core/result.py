"""Resultado estructurado de una ejecución."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from editorial_ia.core.context import ensure_utc, validate_project_id, validate_runtime_id
from editorial_ia.core.contracts import AgentOutput, ValidationIssue


class AgentResultStatus(StrEnum):
    SUCCESS = "SUCCESS"
    REQUIRES_CHANGES = "REQUIRES_CHANGES"
    REJECTED = "REJECTED"
    FAILED = "FAILED"
    ESCALATED = "ESCALATED"


class AgentResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    agent_id: str
    project_id: str
    execution_id: str
    event_id: str
    agent_version: str
    status: AgentResultStatus
    started_at: datetime
    finished_at: datetime
    output: AgentOutput | None
    warnings: tuple[ValidationIssue, ...] = ()
    errors: tuple[ValidationIssue, ...] = ()
    evidence: tuple[str, ...] = ()
    next_recommended_action: str | None = None
    retryable: bool
    attempt_count: int = Field(ge=0)
    audit_reference: str

    @field_validator("project_id")
    @classmethod
    def project_id_is_valid(cls, value: str) -> str:
        if not validate_project_id(value):
            raise ValueError("project_id no cumple el formato admitido.")
        return value

    @field_validator("execution_id")
    @classmethod
    def execution_id_is_valid(cls, value: str) -> str:
        if not validate_runtime_id(value, "execution"):
            raise ValueError("execution_id no es válido.")
        return value

    @field_validator("event_id")
    @classmethod
    def event_id_is_valid(cls, value: str) -> str:
        if not validate_runtime_id(value, "event"):
            raise ValueError("event_id no es válido.")
        return value

    @field_validator("audit_reference")
    @classmethod
    def audit_reference_is_valid(cls, value: str) -> str:
        if not validate_runtime_id(value, "audit"):
            raise ValueError("audit_reference no es válido.")
        return value

    @field_validator("started_at", "finished_at")
    @classmethod
    def timestamps_are_utc(cls, value: datetime) -> datetime:
        return ensure_utc(value)
