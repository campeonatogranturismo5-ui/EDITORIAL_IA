"""Abstracción común de agente."""

from __future__ import annotations

from abc import ABC, abstractmethod

from editorial_ia.core.context import AgentContext
from editorial_ia.core.contracts import (
    AgentInput,
    AgentMetadata,
    AgentOutput,
    ValidationIssue,
)


class BaseAgent(ABC):
    """Contrato mínimo de todos los agentes ejecutables."""

    @property
    @abstractmethod
    def metadata(self) -> AgentMetadata:
        """Metadatos inmutables del agente."""

    @property
    def agent_id(self) -> str:
        return self.metadata.agent_id

    @property
    def name(self) -> str:
        return self.metadata.name

    @property
    def version(self) -> str:
        return self.metadata.version

    @property
    def layer(self) -> str:
        return self.metadata.layer.value

    @property
    def description(self) -> str:
        return self.metadata.description

    def validate_input(self, agent_input: AgentInput) -> tuple[ValidationIssue, ...]:
        return ()

    @abstractmethod
    def execute(self, context: AgentContext, agent_input: AgentInput) -> AgentOutput:
        """Ejecuta una tarea local y devuelve una salida estructurada."""

    def validate_output(self, output: AgentOutput) -> tuple[ValidationIssue, ...]:
        return ()

    def get_capabilities(self) -> tuple[str, ...]:
        return self.metadata.capabilities

    def get_metadata(self) -> AgentMetadata:
        return self.metadata


Agent = BaseAgent
