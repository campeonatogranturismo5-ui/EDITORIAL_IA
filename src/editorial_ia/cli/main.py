"""CLI mínima para la infraestructura local."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Sequence

from editorial_ia.agents import EchoTestAgent
from editorial_ia.core.audit import AuditLogger
from editorial_ia.core.errors import AgentNotFoundError
from editorial_ia.core.registry import AgentRegistry
from editorial_ia.core.result import AgentResultStatus
from editorial_ia.core.runner import AgentRunner


def build_registry() -> AgentRegistry:
    registry = AgentRegistry()
    registry.register(EchoTestAgent())
    return registry


def default_audit_directory() -> Path:
    configured = os.environ.get("EDITORIAL_IA_AUDIT_DIR")
    return Path(configured) if configured else Path("AUDITORIAS/eventos")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="editorial-ia")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Ejecuta un agente registrado.")
    run_parser.add_argument("--agent", required=True)
    run_parser.add_argument("--project", required=True)
    run_parser.add_argument("--input", required=True)
    run_parser.add_argument("--audit-dir", type=Path, default=None)

    subparsers.add_parser("list-agents", help="Lista los agentes registrados.")

    show_parser = subparsers.add_parser("show-agent", help="Muestra un agente.")
    show_parser.add_argument("agent_id")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    registry = build_registry()

    if args.command == "list-agents":
        data = [item.model_dump(mode="json") for item in registry.list_agents()]
        print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    if args.command == "show-agent":
        try:
            metadata = registry.get_metadata(args.agent_id)
        except AgentNotFoundError as exc:
            print(json.dumps({"error": exc.code, "message": str(exc)}, ensure_ascii=False, indent=2))
            return 1
        print(metadata.model_dump_json(indent=2))
        return 0

    audit_directory = args.audit_dir or default_audit_directory()
    runner = AgentRunner(registry, AuditLogger(audit_directory))
    result = runner.run(
        agent_id=args.agent,
        project_id=args.project,
        payload={"text": args.input},
        metadata={"interface": "cli"},
    )
    print(result.model_dump_json(indent=2))
    return 0 if result.status == AgentResultStatus.SUCCESS else 1


if __name__ == "__main__":
    raise SystemExit(main())
