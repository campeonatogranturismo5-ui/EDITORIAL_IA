from __future__ import annotations

import pytest

from editorial_ia.agents import EchoTestAgent
from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.runner import AgentRunner


@pytest.fixture
def registry() -> AgentRegistry:
    value = AgentRegistry()
    value.register(EchoTestAgent())
    return value


@pytest.fixture
def audit_logger(tmp_path) -> AuditLogger:
    return AuditLogger(tmp_path / "audit")


@pytest.fixture
def runner(registry: AgentRegistry, audit_logger: AuditLogger) -> AgentRunner:
    return AgentRunner(registry, audit_logger)
