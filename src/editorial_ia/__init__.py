"""Infraestructura local mínima de Editorial IA."""

from editorial_ia.core.agent import Agent, BaseAgent
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.runner import AgentRunner

__all__ = ["Agent", "BaseAgent", "AgentRegistry", "AgentRunner"]
__version__ = "0.1.0"
