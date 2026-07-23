"""Identificadores y contexto inmutable de ejecución."""

from __future__ import annotations

import re
import secrets
from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

PROJECT_ID_PATTERN = re.compile(r"^PID-\d{8}-[A-Za-z0-9]{4}$")
PILOT_PROJECT_ID = "PID-PILOTO-001"
RUNTIME_ID_PATTERNS = {
    "execution": re.compile(r"^EXE-[0-9a-f]{32}$"),
    "event": re.compile(r"^EVT-[0-9a-f]{32}$"),
    "audit": re.compile(r"^AUD-[0-9a-f]{32}$"),
}


def utc_now() -> datetime:
    """Devuelve una fecha consciente de zona en UTC."""

    return datetime.now(UTC)


def ensure_utc(value: datetime) -> datetime:
    """Normaliza una fecha consciente de zona a UTC."""

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("El tiempo debe incluir zona horaria.")
    return value.astimezone(UTC)


def generate_project_id(*, now: datetime | None = None) -> str:
    instant = ensure_utc(now) if now is not None else utc_now()
    suffix = secrets.token_hex(2).upper()
    return f"PID-{instant:%Y%m%d}-{suffix}"


def validate_project_id(project_id: str, *, allow_pilot: bool = True) -> bool:
    return bool(PROJECT_ID_PATTERN.fullmatch(project_id)) or (
        allow_pilot and project_id == PILOT_PROJECT_ID
    )


def _generate_runtime_id(prefix: str) -> str:
    return f"{prefix}-{secrets.token_hex(16)}"


def generate_execution_id() -> str:
    return _generate_runtime_id("EXE")


def generate_event_id() -> str:
    return _generate_runtime_id("EVT")


def generate_audit_id() -> str:
    return _generate_runtime_id("AUD")


def validate_runtime_id(value: str, kind: str) -> bool:
    pattern = RUNTIME_ID_PATTERNS.get(kind)
    if pattern is None:
        raise ValueError(f"Tipo de identificador desconocido: {kind}")
    return bool(pattern.fullmatch(value))


class AgentContext(BaseModel):
    """Contexto estructurado creado por el runner."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    project_id: str
    execution_id: str
    event_id: str
    agent_id: str
    agent_version: str
    started_at: datetime
    attempt: int = Field(ge=1)
    timeout_seconds: float = Field(gt=0)
    metadata: dict[str, Any] = Field(default_factory=dict)

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

    @field_validator("started_at")
    @classmethod
    def started_at_is_utc(cls, value: datetime) -> datetime:
        return ensure_utc(value)
