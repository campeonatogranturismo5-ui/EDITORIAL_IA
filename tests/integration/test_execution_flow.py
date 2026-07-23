from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.result import AgentResultStatus
from editorial_ia.core.runner import AgentRunner


def test_register_execute_validate_and_audit(registry, tmp_path) -> None:
    logger = AuditLogger(tmp_path / "events")
    runner = AgentRunner(registry, logger)
    result = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": "Prueba de infraestructura"},
        metadata={"case": "integration"},
    )

    assert result.status == AgentResultStatus.SUCCESS
    assert result.output.data["text"] == "Prueba de infraestructura"
    assert result.output.data["character_count"] == len(
        "Prueba de infraestructura"
    )
    assert "input_validation_executed:true" in result.evidence
    records = logger.read(
        project_id="PID-PILOTO-001",
        agent_id="TEST-AGENT-001",
        execution_id=result.execution_id,
    )
    assert len(records) == 1
    assert logger.checksum_is_valid(records[0])


def test_audits_append_instead_of_overwrite(registry, tmp_path) -> None:
    logger = AuditLogger(tmp_path / "events")
    runner = AgentRunner(registry, logger)
    first = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": "uno"},
    )
    second = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": "dos"},
    )
    assert first.execution_id != second.execution_id
    assert len(logger.path.read_text(encoding="utf-8").splitlines()) == 2
    assert len(logger.read(project_id="PID-PILOTO-001")) == 2


def test_empty_and_missing_agent_are_audited(registry, tmp_path) -> None:
    logger = AuditLogger(tmp_path / "events")
    runner = AgentRunner(registry, logger)
    empty = runner.run(
        agent_id="TEST-AGENT-001",
        project_id="PID-PILOTO-001",
        payload={"text": " "},
    )
    missing = runner.run(
        agent_id="TEST-AGENT-999",
        project_id="PID-PILOTO-001",
        payload={"text": "x"},
    )
    assert empty.status == AgentResultStatus.REJECTED
    assert missing.status == AgentResultStatus.FAILED
    assert len(logger.read()) == 2
