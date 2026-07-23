# Decisiones del piloto

## DEC-PIL-001 — Mantener el estado persistido en IDEA

- **Estado:** aplicado
- **Motivo:** probar transiciones sin afirmar que ocurrió un flujo editorial real.
- **Fuente:** paso 7 autorizado.

## DEC-PIL-002 — No resolver la posición de GR-1

- **Estado:** aplicado
- **Motivo:** la arquitectura mantiene esa posición pendiente de validación.
- **Consecuencia:** las pruebas de rechazo utilizan GR-2 y GR-3.

## DEC-PIL-003 — Versionar en lugar de sobrescribir

- **Estado:** aplicado
- **Motivo:** preservar reversibilidad y trazabilidad.
- **Evidencia:** `manuscrito/ms_capitulo_01_v01.md` y `manuscrito/ms_capitulo_01_v02.md`.
