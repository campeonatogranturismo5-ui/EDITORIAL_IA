"""Errores públicos y clasificables de la infraestructura."""


class EditorialIAError(Exception):
    """Error base controlado."""

    code = "EDITORIAL_IA_ERROR"


class DuplicateAgentError(EditorialIAError):
    code = "DUPLICATE_AGENT"


class AgentNotFoundError(EditorialIAError):
    code = "AGENT_NOT_FOUND"


class InvalidContractError(EditorialIAError):
    code = "INVALID_CONTRACT"


class InvalidInputError(EditorialIAError):
    code = "INVALID_INPUT"


class InvalidOutputError(EditorialIAError):
    code = "INVALID_OUTPUT"


class AgentExecutionError(EditorialIAError):
    code = "AGENT_EXECUTION_FAILED"


class EscalationRequiredError(EditorialIAError):
    code = "ESCALATION_REQUIRED"


class LogicalTimeoutError(AgentExecutionError):
    code = "LOGICAL_TIMEOUT"
