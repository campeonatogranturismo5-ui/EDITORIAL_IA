# ADR-0004 — Infraestructura base para agentes

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado:** `DEFINIDO`
- **Fuente:** paso 9 autorizado, `../ARQUITECTURA_SISTEMA.md` y `../../INFORMES/AUDITORIA_FASE_INICIAL.md`
- **Responsable de aprobación:** Responsable Técnico y responsable humano

## Contexto

El repositorio contenía documentación y pruebas documentales, pero ningún núcleo ejecutable. El paso 9 autoriza una infraestructura local mínima y un único agente ficticio. No autoriza agentes editoriales reales, servicios externos, bases de datos, concurrencia ni bus de eventos.

La instrucción propuso el nombre `ADR-0003-infraestructura-base-agentes.md`, pero `ADR-0003` ya identifica la decisión de votación del Consejo. Para preservar unicidad y trazabilidad se usa el siguiente identificador disponible: `ADR-0004`.

## Decisión

Se adopta:

- Python 3.12 o superior;
- estructura `src/editorial_ia/`;
- Pydantic 2 para contratos y validación;
- Pytest para pruebas;
- JSON para entradas y resultados;
- JSONL local append-only para auditoría;
- `pathlib` para rutas;
- tipado explícito y abstracciones pequeñas;
- registro explícito de agentes;
- ejecución local, síncrona y sin red.

Las pruebas técnicas nuevas se ubican en `tests/`, siguiendo la convención del ecosistema Python. Las pruebas documentales existentes permanecen en `TEST/`; ambas áreas conservan propósitos distintos.

## Alternativas consideradas

### Solo biblioteca estándar

Descartada para los contratos públicos porque Pydantic reduce ambigüedad, genera errores estructurados y serializa de forma consistente. La biblioteca estándar sigue siendo preferente para IDs, archivos, checksums, CLI y tiempos.

### JavaScript o TypeScript

Descartado porque el repositorio no tenía tecnología previa y el paso 9 prescribe Python cuando no existe una.

### Framework web o base de datos

Descartados por alcance, complejidad y prohibición expresa.

### Descubrimiento automático de plugins

Descartado por seguridad. El registro es explícito y no importa módulos arbitrarios.

## Ventajas

- Contratos verificables y serializables.
- Núcleo pequeño, desacoplado y sustituible.
- Pruebas deterministas sin Internet.
- Auditoría legible y portable.
- Ejecución reproducible desde CLI.
- Separación clara entre infraestructura y agentes editoriales.

## Riesgos

- JSONL no ofrece transacciones, bloqueo multiproceso ni inmutabilidad criptográfica.
- El timeout es lógico: detecta exceso después de una ejecución síncrona, pero no puede interrumpirla.
- Los reintentos son locales y no sobreviven a fallos de proceso.
- Pydantic es una dependencia externa.
- El enmascaramiento reduce exposición accidental, pero no sustituye un gestor de secretos.

## Consecuencias

- `TEST-AGENT-001` es el único agente ejecutable y está marcado `TEST_ONLY`.
- Los 44 perfiles documentales permanecen no implementados.
- La infraestructura no decide estados editoriales ni puertas humanas.
- Las auditorías locales se guardan en `AUDITORIAS/eventos/`.
- Cualquier ampliación operativa requiere nuevas decisiones, controles y pruebas.

## Sustitución futura

La tecnología puede sustituirse preservando los contratos JSON y los identificadores públicos:

1. congelar las versiones de los esquemas;
2. crear adaptadores para registro, runner y auditoría;
3. ejecutar las mismas pruebas contractuales contra ambas implementaciones;
4. migrar registros sin alterar `audit_id`, `execution_id` ni checksum;
5. aprobar la sustitución mediante una nueva ADR;
6. retirar la implementación anterior solo después de una regresión completa.
