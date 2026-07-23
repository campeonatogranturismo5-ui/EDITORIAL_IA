from datetime import UTC, datetime

import pytest

from editorial_ia.core.context import (
    PILOT_PROJECT_ID,
    generate_audit_id,
    generate_event_id,
    generate_execution_id,
    generate_project_id,
    validate_project_id,
    validate_runtime_id,
)


def test_generate_and_validate_production_project_id() -> None:
    project_id = generate_project_id(now=datetime(2026, 7, 23, tzinfo=UTC))
    assert project_id.startswith("PID-20260723-")
    assert validate_project_id(project_id)


def test_pilot_project_id_is_explicitly_accepted() -> None:
    assert validate_project_id(PILOT_PROJECT_ID)
    assert not validate_project_id(PILOT_PROJECT_ID, allow_pilot=False)


@pytest.mark.parametrize(
    ("factory", "kind"),
    [
        (generate_execution_id, "execution"),
        (generate_event_id, "event"),
        (generate_audit_id, "audit"),
    ],
)
def test_runtime_identifiers(factory, kind) -> None:
    first = factory()
    second = factory()
    assert first != second
    assert validate_runtime_id(first, kind)


def test_unknown_runtime_identifier_kind_is_rejected() -> None:
    with pytest.raises(ValueError):
        validate_runtime_id("X", "unknown")
