# Contrato de entrada de agente

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../MANUAL/ARQUITECTURA_SISTEMA.md` y `../AGENTS/_TEMPLATE/AGENT_TEMPLATE.md`
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Finalidad

Normalizar la entrega de trabajo a cualquier agente y permitir que el receptor valide contexto, autoridad, integridad y trazabilidad.

## Sobre obligatorio

| Campo | Requisito |
|---|---|
| `contract_version` | Versión de este contrato |
| `event_id` | Identificador único de entrega |
| `timestamp` | Fecha y hora con zona |
| `project_id` | PID válido |
| `from_agent` | Emisor autorizado |
| `to_agent` | Receptor exacto |
| `task_type` | Tipo de tarea aprobado |
| `project_state` | Estado actual |
| `attempt` | Número de intento |
| `payload_refs` | Referencias versionadas a artefactos |
| `required_sources` | Normas y Memoria que deben consultarse |
| `human_gate` | Puerta y aprobación aplicable, o `NO_APLICA` |
| `constraints` | Límites explícitos |
| `acceptance_criteria` | Criterios verificables |
| `audit_ref` | Referencia al registro de auditoría |

## Validación

1. Todos los campos obligatorios están presentes.
2. PID, agentes, estado e intento tienen formato válido.
3. Los artefactos referenciados existen y su versión es inequívoca.
4. La transición y la tarea están autorizadas.
5. Las aprobaciones humanas necesarias están presentes.
6. No hay secretos embebidos.

## Resultados

- `ENTRADA_ACEPTADA`: puede procesarse.
- `ENTRADA_RECHAZADA`: emitir [informe de rechazo](informe-rechazo.md).
- `ENTRADA_BLOQUEADA`: escalar por falta de decisión o acceso.

## Ejemplo no ejecutable

```yaml
contract_version: "1.0"
event_id: "EJEMPLO"
timestamp: "AAAA-MM-DDTHH:MM:SSZ"
project_id: "PID-AAAAMMDD-XXXX"
from_agent: "GOB-01"
to_agent: "OPS-XX"
task_type: "EJEMPLO"
project_state: "PENDIENTE"
attempt: 1
payload_refs: []
required_sources: []
human_gate: "NO_APLICA"
constraints: []
acceptance_criteria: []
audit_ref: "PENDIENTE"
```
