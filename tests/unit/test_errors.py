from pydantic import ValidationError

from editorial_ia.core.contracts import ValidationIssue
from editorial_ia.core.errors import InvalidInputError
from editorial_ia.core.validation import classify_exception, error_issues, is_json_serializable


def test_error_classification() -> None:
    assert classify_exception(InvalidInputError("mal")).code == "INVALID_INPUT"
    assert classify_exception(RuntimeError("boom")).code == "UNHANDLED_EXECUTION_ERROR"

    try:
        ValidationIssue(code="", message="")
    except ValidationError as exc:
        assert classify_exception(exc).code == "PYDANTIC_VALIDATION_ERROR"


def test_json_serialization_and_error_filter() -> None:
    issue = ValidationIssue(code="X", message="error")
    assert is_json_serializable({"ok": [1, 2]})
    assert not is_json_serializable({"bad": object()})
    assert error_issues((issue,)) == (issue,)
