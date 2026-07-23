"""Agente ficticio que valida la infraestructura común."""

from __future__ import annotations

from editorial_ia.core.agent import BaseAgent
from editorial_ia.core.context import AgentContext
from editorial_ia.core.contracts import (
    AgentAvailability,
    AgentInput,
    AgentLayer,
    AgentMetadata,
    AgentOutput,
    ValidationIssue,
)


class EchoTestAgent(BaseAgent):
    """Eco local sin capacidad editorial."""

    _metadata = AgentMetadata(
        agent_id="TEST-AGENT-001",
        name="Agente Eco de Prueba",
        version="1.0.0",
        layer=AgentLayer.TEST,
        description="Agente ficticio para validar contratos, ejecución y auditoría.",
        availability=AgentAvailability.TEST_ONLY,
        capabilities=("echo_text", "count_characters", "validate_non_empty_text"),
    )

    @property
    def metadata(self) -> AgentMetadata:
        return self._metadata

    def validate_input(self, agent_input: AgentInput) -> tuple[ValidationIssue, ...]:
        text = agent_input.payload.get("text")
        if not isinstance(text, str):
            return (
                ValidationIssue(
                    code="TEXT_REQUIRED",
                    field="payload.text",
                    message="payload.text debe ser una cadena.",
                ),
            )
        if not text.strip():
            return (
                ValidationIssue(
                    code="TEXT_EMPTY",
                    field="payload.text",
                    message="payload.text no puede estar vacío.",
                ),
            )
        return ()

    def execute(self, context: AgentContext, agent_input: AgentInput) -> AgentOutput:
        text = str(agent_input.payload["text"])
        return AgentOutput(
            data={
                "text": text,
                "character_count": len(text),
                "test_only": True,
            },
            evidence=(
                "input_validation_executed:true",
                f"execution_attempt:{context.attempt}",
            ),
        )

    def validate_output(self, output: AgentOutput) -> tuple[ValidationIssue, ...]:
        text = output.data.get("text")
        count = output.data.get("character_count")
        if not isinstance(text, str) or count != len(text):
            return (
                ValidationIssue(
                    code="INVALID_CHARACTER_COUNT",
                    field="data.character_count",
                    message="El número de caracteres no coincide con el texto.",
                ),
            )
        if "input_validation_executed:true" not in output.evidence:
            return (
                ValidationIssue(
                    code="MISSING_VALIDATION_EVIDENCE",
                    field="evidence",
                    message="Falta evidencia de validación de entrada.",
                ),
            )
        return ()
