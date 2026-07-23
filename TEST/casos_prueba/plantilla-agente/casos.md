# Casos documentales de plantilla de agente

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../../../AGENTS/_TEMPLATE/AGENT_TEMPLATE.md`
- **Responsable de aprobación:** Responsable de Calidad

## CP-AGT-001 — Ficha completa

- **Preparación:** copia íntegra de la plantilla con campos sustituidos.
- **Esperado:** `SUPERADA`.

## CP-AGT-002 — Falta identificador

- **Preparación:** eliminar `## 1. Identificador`.
- **Esperado:** `FALLIDA`, motivo `SECCION_AUSENTE`.

## CP-AGT-003 — Sección duplicada

- **Preparación:** repetir `## 19. Criterios de aceptación`.
- **Esperado:** `FALLIDA`, motivo `SECCION_DUPLICADA`.

## CP-AGT-004 — Entrada obligatoria vacía

- **Preparación:** mantener el encabezado sin campos ni justificación.
- **Esperado:** `FALLIDA`, motivo `SECCION_VACIA`.

## CP-AGT-005 — Sección no aplicable justificada

- **Preparación:** indicar `NO_APLICA` y la fuente que justifica la excepción.
- **Esperado:** `SUPERADA`.

## CP-AGT-006 — Reintentos sin límite

- **Preparación:** eliminar el número máximo.
- **Esperado:** `FALLIDA`, motivo `CONTRATO_INCOMPLETO`.

## CP-AGT-007 — Escalado humano ausente

- **Preparación:** eliminar las condiciones de escalado.
- **Esperado:** `FALLIDA`, motivo `CONTROL_HUMANO_AUSENTE`.

## Estado de ejecución

Casos definidos documentalmente. Solo CP-AGT-001 se ejecutará contra la plantilla en esta fase; las mutaciones negativas permanecen como especificación reproducible y no alteran la plantilla versionada.
