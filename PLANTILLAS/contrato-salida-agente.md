# Contrato de salida de agente

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../MANUAL/ARQUITECTURA_SISTEMA.md` y `../AGENTS/_TEMPLATE/AGENT_TEMPLATE.md`
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Finalidad

Normalizar la entrega de resultados y permitir validación downstream y auditoría.

## Sobre obligatorio

| Campo | Requisito |
|---|---|
| `contract_version` | Versión del contrato |
| `event_id` | Entrega que originó la ejecución |
| `execution_id` | Ejecución única |
| `timestamp` | Fecha y hora con zona |
| `project_id` | PID |
| `agent_id` | Productor |
| `agent_version` | Versión de ficha y prompt aplicables |
| `attempt` | Intento |
| `status` | `COMPLETADO`, `RECHAZADO`, `ERROR` o `ESCALADO` |
| `artifact_refs` | Artefactos generados, versionados |
| `validation_results` | Autocomprobaciones y evidencias |
| `sources_used` | Documentos consultados |
| `decisions` | Decisiones dentro de autoridad y justificación |
| `warnings` | Riesgos o limitaciones |
| `next_agent` | Receptor previsto o `NINGUNO` |
| `audit_ref` | Registro de auditoría |

## Reglas

- No incluir el contenido completo si basta una referencia versionada.
- No declarar `COMPLETADO` si falla un criterio de aceptación.
- Diferenciar advertencia, rechazo, error y escalado.
- No ocultar reintentos ni validaciones fallidas.
- No incluir secretos.

## Ejemplo no ejecutable

```yaml
contract_version: "1.0"
event_id: "EJEMPLO"
execution_id: "EJEMPLO"
timestamp: "AAAA-MM-DDTHH:MM:SSZ"
project_id: "PID-AAAAMMDD-XXXX"
agent_id: "OPS-XX"
agent_version: "0.0.0"
attempt: 1
status: "ESCALADO"
artifact_refs: []
validation_results: []
sources_used: []
decisions: []
warnings:
  - "EJEMPLO_NO_EJECUTABLE"
next_agent: "NINGUNO"
audit_ref: "PENDIENTE"
```
