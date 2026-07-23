"""Modelos Pydantic para metadatos, entradas, salidas y auditoría."""

from __future__ import annotations

import json
from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from editorial_ia.core.context import (
    ensure_utc,
    validate_project_id,
    validate_runtime_id,
)


class AgentLayer(StrEnum):
    GOVERNANCE = "GOVERNANCE"
    CREATIVE = "CREATIVE"
    EDITORIAL = "EDITORIAL"
    COMMERCIAL = "COMMERCIAL"
    SUPPORT = "SUPPORT"
    TEST = "TEST"


class AgentAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    TEST_ONLY = "TEST_ONLY"


class IssueSeverity(StrEnum):
    WARNING = "WARNING"
    ERROR = "ERROR"


class ValidationIssue(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    field: str | None = None
    severity: IssueSeverity = IssueSeverity.ERROR


class AgentMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    agent_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    version: str = Field(pattern=r"^\d+\.\d+\.\d+$")
    layer: AgentLayer
    description: str = Field(min_length=1)
    availability: AgentAvailability
    capabilities: tuple[str, ...] = ()


class AgentInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    project_id: str
    event_id: str
    payload: dict[str, Any]
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("project_id")
    @classmethod
    def project_id_is_valid(cls, value: str) -> str:
        if not validate_project_id(value):
            raise ValueError("project_id no cumple el formato admitido.")
        return value

    @field_validator("event_id")
    @classmethod
    def event_id_is_valid(cls, value: str) -> str:
        if not validate_runtime_id(value, "event"):
            raise ValueError("event_id no es válido.")
        return value

    @field_validator("payload", "metadata")
    @classmethod
    def content_is_json_serializable(cls, value: dict[str, Any]) -> dict[str, Any]:
        try:
            json.dumps(value, ensure_ascii=False)
        except (TypeError, ValueError) as exc:
            raise ValueError("El contenido debe ser serializable como JSON.") from exc
        return value


class AgentOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    data: dict[str, Any]
    evidence: tuple[str, ...] = ()

    @field_validator("data")
    @classmethod
    def data_is_json_serializable(cls, value: dict[str, Any]) -> dict[str, Any]:
        try:
            json.dumps(value, ensure_ascii=False)
        except (TypeError, ValueError) as exc:
            raise ValueError("La salida debe ser serializable como JSON.") from exc
        return value


class AuditRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    audit_id: str
    execution_id: str
    event_id: str
    project_id: str
    agent_id: str
    agent_version: str
    status: str
    started_at: datetime
    finished_at: datetime
    attempt_count: int = Field(ge=0)
    input: dict[str, Any]
    output: dict[str, Any] | None
    warnings: tuple[dict[str, Any], ...] = ()
    errors: tuple[dict[str, Any], ...] = ()
    evidence: tuple[str, ...] = ()
    next_recommended_action: str | None = None
    retryable: bool
    checksum: str | None = None

    @field_validator("audit_id")
    @classmethod
    def audit_id_is_valid(cls, value: str) -> str:
        if not validate_runtime_id(value, "audit"):
            raise ValueError("audit_id no es válido.")
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

    @field_validator("project_id")
    @classmethod
    def project_id_is_valid(cls, value: str) -> str:
        if not validate_project_id(value):
            raise ValueError("project_id no cumple el formato admitido.")
        return value

    @field_validator("started_at", "finished_at")
    @classmethod
    def timestamps_are_utc(cls, value: datetime) -> datetime:
        return ensure_utc(value)
