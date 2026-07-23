"""Registro local y explícito de agentes."""

from __future__ import annotations

from editorial_ia.core.agent import BaseAgent
from editorial_ia.core.contracts import AgentMetadata
from editorial_ia.core.errors import AgentNotFoundError, DuplicateAgentError


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        agent_id = agent.agent_id
        if agent_id in self._agents:
            raise DuplicateAgentError(f"El agente {agent_id} ya está registrado.")
        self._agents[agent_id] = agent

    def get(self, agent_id: str) -> BaseAgent:
        try:
            return self._agents[agent_id]
        except KeyError as exc:
            raise AgentNotFoundError(f"El agente {agent_id} no existe.") from exc

    def list_agents(self) -> tuple[AgentMetadata, ...]:
        return tuple(
            self._agents[agent_id].get_metadata()
            for agent_id in sorted(self._agents)
        )

    def get_metadata(self, agent_id: str) -> AgentMetadata:
        return self.get(agent_id).get_metadata()

    def is_available(self, agent_id: str) -> bool:
        return agent_id in self._agents

    def remove(self, agent_id: str) -> BaseAgent:
        try:
            return self._agents.pop(agent_id)
        except KeyError as exc:
            raise AgentNotFoundError(f"El agente {agent_id} no existe.") from exc
