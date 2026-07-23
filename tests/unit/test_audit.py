import json
from datetime import UTC, datetime, timedelta

from editorial_ia.core.audit import AuditLogger, REDACTED, mask_secrets
from editorial_ia.core.context import generate_audit_id, generate_event_id, generate_execution_id
from editorial_ia.core.contracts import AuditRecord


def make_record(*, project_id: str = "PID-PILOTO-001", agent_id: str = "TEST-AGENT-001") -> AuditRecord:
    now = datetime(2026, 7, 23, 10, tzinfo=UTC)
    return AuditRecord(
        audit_id=generate_audit_id(),
        execution_id=generate_execution_id(),
        event_id=generate_event_id(),
        project_id=project_id,
        agent_id=agent_id,
        agent_version="1.0.0",
        status="SUCCESS",
        started_at=now,
        finished_at=now,
        attempt_count=1,
        input={"payload": {"text": "hola", "api_key": "secreto"}},
        output={"data": {"authorization": "Bearer abcdefghijk"}},
        retryable=False,
    )


def test_audit_append_read_filter_and_checksum(tmp_path) -> None:
    logger = AuditLogger(tmp_path / "events")
    first = logger.persist(make_record())
    second = logger.persist(make_record(project_id="PID-20260723-A1B2"))

    lines = logger.path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert all(json.loads(line)["checksum"].startswith("sha256:") for line in lines)
    assert logger.checksum_is_valid(first)
    assert logger.checksum_is_valid(second)
    assert logger.read(project_id="PID-PILOTO-001") == (first,)
    assert logger.read(agent_id="TEST-AGENT-001") == (first, second)
    assert logger.read(execution_id=second.execution_id) == (second,)
    assert logger.read(
        started_from=datetime(2026, 7, 23, 9, tzinfo=UTC),
        started_to=datetime(2026, 7, 23, 11, tzinfo=UTC),
    ) == (first, second)
    assert tuple(logger.iter_records()) == (first, second)


def test_audit_masks_secrets_without_overwriting(tmp_path) -> None:
    logger = AuditLogger(tmp_path / "events")
    persisted = logger.persist(make_record())
    assert persisted.input["payload"]["api_key"] == REDACTED
    assert persisted.output["data"]["authorization"] == REDACTED
    assert "secreto" not in logger.path.read_text(encoding="utf-8")
    assert "Bearer" not in logger.path.read_text(encoding="utf-8")


def test_mask_secrets_handles_nested_values() -> None:
    data = {
        "password": "uno",
        "nested": ["ghp_abcdefghijk", {"safe": "Bearer abcdefghijk"}],
        "normal": "visible",
    }
    masked = mask_secrets(data)
    assert masked["password"] == REDACTED
    assert masked["nested"] == [REDACTED, {"safe": REDACTED}]
    assert masked["normal"] == "visible"
