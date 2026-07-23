from editorial_ia.agents import EchoTestAgent
from editorial_ia.core.context import (
    AgentContext,
    generate_event_id,
    generate_execution_id,
    utc_now,
)
from editorial_ia.core.contracts import AgentInput


def test_echo_agent_validates_executes_and_validates_output() -> None:
    agent = EchoTestAgent()
    agent_input = AgentInput(
        project_id="PID-PILOTO-001",
        event_id=generate_event_id(),
        payload={"text": "Eco"},
    )
    context = AgentContext(
        project_id=agent_input.project_id,
        execution_id=generate_execution_id(),
        event_id=agent_input.event_id,
        agent_id=agent.agent_id,
        agent_version=agent.version,
        started_at=utc_now(),
        attempt=1,
        timeout_seconds=1,
    )

    assert agent.validate_input(agent_input) == ()
    output = agent.execute(context, agent_input)
    assert output.data == {"text": "Eco", "character_count": 3, "test_only": True}
    assert agent.validate_output(output) == ()
    assert agent.get_capabilities()
    assert agent.get_metadata().agent_id == "TEST-AGENT-001"


def test_echo_agent_rejects_empty_and_non_string_text() -> None:
    agent = EchoTestAgent()
    empty = AgentInput(
        project_id="PID-PILOTO-001",
        event_id=generate_event_id(),
        payload={"text": "   "},
    )
    missing = AgentInput(
        project_id="PID-PILOTO-001",
        event_id=generate_event_id(),
        payload={},
    )
    assert agent.validate_input(empty)[0].code == "TEXT_EMPTY"
    assert agent.validate_input(missing)[0].code == "TEXT_REQUIRED"
