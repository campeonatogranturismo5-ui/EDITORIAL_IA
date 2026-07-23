"""Auditoría JSONL local, append-only y con enmascaramiento."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from threading import Lock
from typing import Any, Iterable

from editorial_ia.core.contracts import AuditRecord

REDACTED = "***REDACTED***"
SENSITIVE_KEY = re.compile(
    r"(password|passwd|secret|token|api[_-]?key|authorization|credential|private[_-]?key)",
    re.IGNORECASE,
)
SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]+", re.IGNORECASE),
    re.compile(r"\b(?:ghp_|gho_|github_pat_|sk-)[A-Za-z0-9_-]{8,}"),
)


def mask_secrets(value: Any, *, key: str | None = None) -> Any:
    if key is not None and SENSITIVE_KEY.search(key):
        return REDACTED
    if isinstance(value, dict):
        return {str(item_key): mask_secrets(item, key=str(item_key)) for item_key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [mask_secrets(item) for item in value]
    if isinstance(value, str):
        masked = value
        for pattern in SENSITIVE_VALUE_PATTERNS:
            masked = pattern.sub(REDACTED, masked)
        return masked
    return value


def calculate_checksum(record: dict[str, Any]) -> str:
    material = dict(record)
    material.pop("checksum", None)
    encoded = json.dumps(
        material,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(encoded).hexdigest()}"


class AuditLogger:
    """Persiste y consulta registros completos e independientes."""

    def __init__(
        self,
        directory: Path | str = Path("AUDITORIAS/eventos"),
        *,
        filename: str = "agent-events.jsonl",
    ) -> None:
        self.directory = Path(directory)
        self.path = self.directory / filename
        self._lock = Lock()

    def persist(self, record: AuditRecord) -> AuditRecord:
        self.directory.mkdir(parents=True, exist_ok=True)
        data = mask_secrets(record.model_dump(mode="json"))
        data["checksum"] = calculate_checksum(data)
        persisted = AuditRecord.model_validate(data)
        line = json.dumps(
            persisted.model_dump(mode="json"),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        with self._lock, self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line)
            handle.write("\n")
        return persisted

    def read(
        self,
        *,
        project_id: str | None = None,
        agent_id: str | None = None,
        execution_id: str | None = None,
        started_from: datetime | None = None,
        started_to: datetime | None = None,
    ) -> tuple[AuditRecord, ...]:
        if not self.path.exists():
            return ()
        records: list[AuditRecord] = []
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                record = AuditRecord.model_validate_json(line)
                if project_id is not None and record.project_id != project_id:
                    continue
                if agent_id is not None and record.agent_id != agent_id:
                    continue
                if execution_id is not None and record.execution_id != execution_id:
                    continue
                if started_from is not None and record.started_at < started_from:
                    continue
                if started_to is not None and record.started_at > started_to:
                    continue
                records.append(record)
        return tuple(records)

    @staticmethod
    def checksum_is_valid(record: AuditRecord) -> bool:
        if record.checksum is None:
            return False
        return record.checksum == calculate_checksum(record.model_dump(mode="json"))

    def iter_records(self) -> Iterable[AuditRecord]:
        return iter(self.read())
