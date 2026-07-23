from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from editorial_ia.core.context import generate_audit_id, generate_event_id, generate_execution_id
from editorial_ia.core.contracts import (
    AgentAvailability,
    AgentInput,
    AgentLayer,
    AgentMetadata,
    AgentOutput,
    ValidationIssue,
)
from editorial_ia.core.result import AgentResult, AgentResultStatus


def test_valid_contracts() -> None:
    metadata = AgentMetadata(
        agent_id="TEST-AGENT-001",
        name="Prueba",
        version="1.0.0",
        layer=AgentLayer.TEST,
        description="Contrato de prueba",
        availability=AgentAvailability.TEST_ONLY,
        capabilities=("echo",),
    )
    agent_input = AgentInput(
        project_id="PID-PILOTO-001",
        event_id=generate_event_id(),
        payload={"text": "hola"},
    )
    output = AgentOutput(data={"text": "hola"}, evidence=("validado",))

    assert metadata.availability == AgentAvailability.TEST_ONLY
    assert agent_input.payload["text"] == "hola"
    assert output.evidence == ("validado",)


@pytest.mark.parametrize(
    ("model", "kwargs"),
    [
        (AgentMetadata, {"agent_id": "", "name": "x", "version": "1", "layer": "TEST", "description": "x", "availability": "TEST_ONLY"}),
        (AgentInput, {"project_id": "INVALIDO", "event_id": "EVT-x", "payload": {}}),
        (AgentOutput, {"data": {"bad": object()}}),
        (ValidationIssue, {"code": "", "message": ""}),
    ],
)
def test_invalid_contracts(model, kwargs) -> None:
    with pytest.raises(ValidationError):
        model(**kwargs)


def test_agent_result_contains_required_traceability() -> None:
    now = datetime(2026, 7, 23, 10, tzinfo=UTC)
    result = AgentResult(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        execution_id=generate_execution_id(),
        event_id=generate_event_id(),
        agent_version="1.0.0",
        status=AgentResultStatus.SUCCESS,
        started_at=now,
        finished_at=now,
        output=AgentOutput(data={"text": "x"}),
        evidence=("validado",),
        next_recommended_action="ninguna",
        retryable=False,
        attempt_count=1,
        audit_reference=generate_audit_id(),
    )

    assert result.started_at.utcoffset().total_seconds() == 0
    assert result.status == AgentResultStatus.SUCCESS
    assert result.audit_reference.startswith("AUD-")


def test_naive_timestamps_are_rejected() -> None:
    with pytest.raises(ValidationError):
        AgentResult(
            agent_id="TEST-AGENT-001",
            project_id="PID-PILOTO-001",
            execution_id=generate_execution_id(),
            event_id=generate_event_id(),
            agent_version="1.0.0",
            status=AgentResultStatus.SUCCESS,
            started_at=datetime(2026, 7, 23),
            finished_at=datetime(2026, 7, 23),
            output=None,
            retryable=False,
            attempt_count=1,
            audit_reference=generate_audit_id(),
        )
