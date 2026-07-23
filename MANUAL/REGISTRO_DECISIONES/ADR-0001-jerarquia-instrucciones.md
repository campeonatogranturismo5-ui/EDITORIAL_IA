# ADR-0001 — Jerarquía de instrucciones

- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** arquitectura editorial IA v2.0 y PASO 3 autorizado
- **Responsable de aprobación:** responsable humano

## Contexto

Codex necesita una regla inequívoca para resolver instrucciones procedentes de la Constitución, los Códigos, la Memoria Editorial, las reglas operativas, las fichas de agentes, los workflows y cada tarea concreta.

## Decisión

Se adopta esta jerarquía, de mayor a menor autoridad:

1. Constitución.
2. Códigos.
3. Memoria Editorial validada.
4. Reglas.
5. Fichas de agentes.
6. Workflows.
7. Instrucción concreta de la tarea.

El `AGENTS.md` raíz establece las reglas transversales. Los `AGENTS.md` locales solo pueden especializar su carpeta y descendientes. No pueden reducir controles, omitir puertas humanas ni contradecir una fuente superior.

Si existe un conflicto no resoluble o falta una decisión humana imprescindible, Codex debe detener la parte afectada, informar del bloqueo y pedir resolución. No puede rellenar el vacío con una decisión editorial inventada.

## Consecuencias

- Las tareas quedan subordinadas a la autoridad documental.
- Las instrucciones locales pueden ser más específicas, pero no incompatibles.
- Toda decisión debe ser trazable.
- Los conflictos se hacen visibles en lugar de resolverse implícitamente.

## Alternativas descartadas

- Dar prioridad absoluta a la última instrucción: permitiría contradecir la Constitución.
- Un único archivo de instrucciones para todo el repositorio: impediría especializar reglas por área.
- Resolver conflictos automáticamente: violaría la regla de no inventar decisiones.

## Comprobación

- Revisar que cada `AGENTS.md` local solo trate su área.
- Comparar prohibiciones y obligaciones con el archivo raíz.
- Confirmar que ninguna instrucción local permite omitir trazabilidad, versionado, seguridad o aprobación humana.

