# ADR-0002 — Plantilla única de agentes

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** arquitectura editorial IA v2.0, PASO 5 autorizado y `ADR-0001`
- **Responsable de aprobación:** responsable humano y Consejo Editorial

## Contexto

La arquitectura define 41 roles conceptuales y 44 perfiles potencialmente ejecutables. Sin una estructura común, sus fichas pueden omitir entradas, prohibiciones, criterios, errores, reintentos, escalado o auditoría.

## Decisión

Toda ficha nueva o desarrollada debe derivarse de `../../AGENTS/_TEMPLATE/AGENT_TEMPLATE.md`.

La plantilla:

- separa identidad, autoridad y estado;
- define entradas, proceso, herramientas y salida;
- exige aceptación, calidad, errores y reintentos;
- conecta agentes anterior y siguiente;
- conserva escalado humano y auditoría;
- exige casos de prueba, ejemplos e historial.

Los contratos de `../../PLANTILLAS/` normalizan entrada, salida, rechazo, error, decisión y comprobación.

## Reglas

- Una ficha incompleta no puede considerarse `DEFINIDO`.
- La plantilla no concede herramientas ni autoridad.
- Los campos no aplicables se justifican; no se eliminan.
- Completar una ficha no implementa el agente.
- Cambiar secciones obligatorias requiere actualizar este ADR, contratos y pruebas.

## Consecuencias

- Mayor uniformidad y validación documental.
- Más trazabilidad entre agentes.
- Posibilidad de automatizar validaciones en una fase posterior.
- Mayor coste inicial de documentación.

## Alternativas descartadas

- Una plantilla por capa: aumenta divergencia.
- Fichas libres: impiden comprobación consistente.
- Esquema solo técnico: omite autoridad editorial y escalado humano.

## Verificación

- [Prueba de secciones obligatorias](../../TEST/unitarios/plantilla-agente/validacion-secciones.md).
- [Casos documentales](../../TEST/casos_prueba/plantilla-agente/casos.md).
