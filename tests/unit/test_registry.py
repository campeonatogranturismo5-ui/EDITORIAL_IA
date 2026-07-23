import pytest

from editorial_ia.agents import EchoTestAgent
from editorial_ia.core.errors import AgentNotFoundError, DuplicateAgentError
from editorial_ia.core.registry import AgentRegistry


def test_register_find_list_metadata_and_availability() -> None:
    registry = AgentRegistry()
    agent = EchoTestAgent()
    registry.register(agent)

    assert registry.get(agent.agent_id) is agent
    assert registry.get_metadata(agent.agent_id).name == "Agente Eco de Prueba"
    assert registry.is_available(agent.agent_id)
    assert [item.agent_id for item in registry.list_agents()] == [agent.agent_id]


def test_duplicate_agent_is_rejected() -> None:
    registry = AgentRegistry()
    registry.register(EchoTestAgent())
    with pytest.raises(DuplicateAgentError):
        registry.register(EchoTestAgent())


def test_missing_agent_and_test_only_removal() -> None:
    registry = AgentRegistry()
    with pytest.raises(AgentNotFoundError):
        registry.get("NO-EXISTE")
    registry.register(EchoTestAgent())
    removed = registry.remove("TEST-AGENT-001")
    assert removed.agent_id == "TEST-AGENT-001"
    assert not registry.is_available("TEST-AGENT-001")
    with pytest.raises(AgentNotFoundError):
        registry.remove("TEST-AGENT-001")
