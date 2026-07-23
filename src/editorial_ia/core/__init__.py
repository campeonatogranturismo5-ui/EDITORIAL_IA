"""Contratos y servicios comunes para agentes locales."""

from editorial_ia.core.agent import Agent, BaseAgent
from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.runner import AgentRunner

__all__ = ["Agent", "BaseAgent", "AuditLogger", "AgentRegistry", "AgentRunner"]
