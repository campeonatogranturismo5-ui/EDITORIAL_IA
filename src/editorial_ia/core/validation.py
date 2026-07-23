"""Utilidades de validación y clasificación de errores."""

from __future__ import annotations

import json
from typing import Any

from pydantic import ValidationError

from editorial_ia.core.contracts import IssueSeverity, ValidationIssue
from editorial_ia.core.errors import EditorialIAError


def is_json_serializable(value: Any) -> bool:
    try:
        json.dumps(value, ensure_ascii=False)
    except (TypeError, ValueError):
        return False
    return True


def classify_exception(exc: Exception) -> ValidationIssue:
    if isinstance(exc, EditorialIAError):
        code = exc.code
    elif isinstance(exc, ValidationError):
        code = "PYDANTIC_VALIDATION_ERROR"
    else:
        code = "UNHANDLED_EXECUTION_ERROR"
    return ValidationIssue(code=code, message=str(exc) or exc.__class__.__name__)


def error_issues(issues: tuple[ValidationIssue, ...]) -> tuple[ValidationIssue, ...]:
    return tuple(issue for issue in issues if issue.severity == IssueSeverity.ERROR)
