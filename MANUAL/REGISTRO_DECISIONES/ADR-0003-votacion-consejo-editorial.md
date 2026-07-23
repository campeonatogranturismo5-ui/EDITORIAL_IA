# ADR-0003 — Votación del Consejo Editorial

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado:** `DEFINIDO` para simulación documental; pendiente de aprobación humana operativa
- **Fuente:** `../CODIGOS/CODIGO_PRODUCCION.md`, `../ARQUITECTURA_SISTEMA.md` y paso 6 autorizado
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Contexto

La arquitectura establece cuatro votos independientes y tres valores posibles, pero deja sin resolver la consolidación completa y alterna entre devolución y escalado para 2-2. El paso 6 exige una regla comprobable sin implementar automatización.

## Decisión

Cada miembro recibe la misma huella de expediente, vota sin ver los votos ajenos, justifica su voto, cita normas y sella el registro antes de la consolidación.

La pareja `A-N` representa votos `APROBAR` frente a votos no aprobatorios (`RECHAZAR` o `REQUIERE_CAMBIOS`):

| Distribución | Resultado consolidado | Tratamiento |
|---|---|---|
| 4-0 | `APROBAR` | pasa a revisión humana si hay GR |
| 3-1 | `APROBAR` | pasa con disidencia registrada |
| 2-2 | `REQUIERE_CAMBIOS` | devolución y escalado humano obligatorio |
| 1-3 | `RECHAZAR` | devolución e incidente E5 documental |
| 0-4 | `RECHAZAR` | devolución e incidente E5 documental |

Un voto no aprobatorio conserva su valor original y su justificación; la consolidación no lo convierte ni lo borra.

GR-1, GR-2, GR-3 y GR-4 requieren siempre decisión humana posterior. Un resultado `APROBAR` del Consejo nunca equivale a aprobación humana. Esta ADR no decide la ubicación controvertida de GR-1.

## Consecuencias

- La consolidación es determinista y reproducible.
- El empate no avanza el flujo y queda visible al humano.
- La disidencia se conserva para métricas y auditoría.
- Los votos se representan como claves fijas para impedir miembros duplicados u omitidos.
- El mecanismo sigue siendo documental y simulado.

## Alternativas descartadas

- Desempate automático por GOB-01: vulnera la independencia y amplía su autoridad.
- Voto de calidad de un consejero: no está autorizado en la fuente.
- Avance automático en 2-2: contradice el principio humano en el bucle.

## Verificación

- `../../TEST/unitarios/consejo-editorial/validar-votaciones.ps1`
- `../../TEST/casos_prueba/consejo-editorial/`
