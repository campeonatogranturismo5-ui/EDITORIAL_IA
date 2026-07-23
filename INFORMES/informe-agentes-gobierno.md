# Informe de agentes de Gobierno

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado:** `COMPLETADO_DOCUMENTALMENTE`
- **Fuente:** arquitectura v2.0 y paso 6 autorizado
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Alcance realizado

Se desarrollaron exclusivamente los seis perfiles de Gobierno:

- `GOB-01` Orquestador Maestro.
- `GOB-02a` Director Editorial.
- `GOB-02b` Responsable de Marketing.
- `GOB-02c` Responsable de Calidad.
- `GOB-02d` Responsable Técnico.
- `GOB-03` Auditor de Calidad.

Cada ficha contiene las 33 secciones de la plantilla oficial, declara su autoridad, entradas, salidas, prohibiciones, reintentos, escalado, auditoría y casos de prueba.

## Consejo Editorial

Los cuatro miembros votan sobre un expediente idéntico y no ven votos ajenos antes de sellar el propio. Cada voto requiere justificación y al menos una referencia normativa.

| Distribución | Consolidación |
|---|---|
| 4-0 | `APROBAR` |
| 3-1 | `APROBAR` con disidencia |
| 2-2 | `REQUIERE_CAMBIOS` y escalado humano |
| 1-3 | `RECHAZAR` e incidente E5 documental |
| 0-4 | `RECHAZAR` e incidente E5 documental |

La decisión completa se registra en `../MANUAL/REGISTRO_DECISIONES/ADR-0003-votacion-consejo-editorial.md`.

## Puertas humanas

GR-1, GR-2, GR-3 y GR-4 permanecen bajo aprobación humana obligatoria. La aprobación del Consejo no sustituye esa decisión. La ubicación exacta de GR-1 continúa pendiente.

## Verificación

- Esquema: `../PLANTILLAS/votacion-consejo.schema.json`.
- Checklist: `../CHECKLISTS/GOB-02_votacion.md`.
- Ejemplos: `../TEST/casos_prueba/consejo-editorial/`.
- Prueba: `../TEST/unitarios/consejo-editorial/validar-votaciones.ps1`.

## Límites

- Las fichas son contratos documentales, no agentes ejecutables.
- Los ejemplos son sintéticos.
- No se conectó ningún modelo de IA.
- No se implementó bus de eventos, automatización, API ni publicación.
- El ICE no se calcula porque su fórmula sigue pendiente de validación.
- No se avanzó al proyecto piloto del paso 7.
