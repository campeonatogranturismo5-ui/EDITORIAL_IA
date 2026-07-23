from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def run_cli(tmp_path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["EDITORIAL_IA_AUDIT_DIR"] = str(tmp_path / "cli-audit")
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[2] / "src")
    return subprocess.run(
        [sys.executable, "-m", "editorial_ia.cli.main", *args],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )


def test_cli_lists_and_shows_only_test_agent(tmp_path) -> None:
    listed = run_cli(tmp_path, "list-agents")
    assert listed.returncode == 0
    list_payload = json.loads(listed.stdout)
    assert [item["agent_id"] for item in list_payload] == ["TEST-AGENT-001"]
    assert list_payload[0]["availability"] == "TEST_ONLY"

    shown = run_cli(tmp_path, "show-agent", "TEST-AGENT-001")
    assert shown.returncode == 0
    assert json.loads(shown.stdout)["name"] == "Agente Eco de Prueba"


def test_cli_executes_and_writes_audit(tmp_path) -> None:
    completed = run_cli(
        tmp_path,
        "run",
        "--agent",
        "TEST-AGENT-001",
        "--project",
        "PID-PILOTO-001",
        "--input",
        "Prueba de infraestructura",
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["status"] == "SUCCESS"
    assert payload["output"]["data"]["character_count"] == len(
        "Prueba de infraestructura"
    )
    audit_path = tmp_path / "cli-audit" / "agent-events.jsonl"
    assert audit_path.exists()
    assert len(audit_path.read_text(encoding="utf-8").splitlines()) == 1


def test_cli_invalid_input_and_missing_agent(tmp_path) -> None:
    empty = run_cli(
        tmp_path,
        "run",
        "--agent",
        "TEST-AGENT-001",
        "--project",
        "PID-PILOTO-001",
        "--input",
        "",
    )
    assert empty.returncode == 1
    assert json.loads(empty.stdout)["status"] == "REJECTED"

    missing = run_cli(tmp_path, "show-agent", "NO-EXISTE")
    assert missing.returncode == 1
    assert json.loads(missing.stdout)["error"] == "AGENT_NOT_FOUND"
