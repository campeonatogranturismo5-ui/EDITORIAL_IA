# Infraestructura base para agentes

- **Versión:** 0.1.0
- **Fecha:** 2026-07-23
- **Estado:** `IMPLEMENTADA_EN_LOCAL`
- **Decisión:** `MANUAL/REGISTRO_DECISIONES/ADR-0004-infraestructura-base-agentes.md`

## Alcance

Este módulo aporta una base local, mínima y trazable para desarrollar agentes en
fases posteriores. No convierte en ejecutables los perfiles documentales de
`AGENTS/`. El único agente disponible es `TEST-AGENT-001`, creado exclusivamente
para verificar la infraestructura.

Quedan fuera de este paso el Orquestador real, el Consejo Editorial, el Auditor,
los perfiles OPS/SUP, los modelos de IA, las APIs, las bases de datos, el bus de
eventos, la web y cualquier automatización de producción.

## Requisitos e instalación

- Python 3.12 o posterior.
- Dependencias de ejecución: Pydantic 2.
- Dependencias de desarrollo: pytest y pytest-cov.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

También se mantienen `requirements.txt` y `requirements-dev.txt`.

## Estructura

```text
src/editorial_ia/
├── agents/example_agent.py
├── cli/main.py
└── core/
    ├── agent.py
    ├── audit.py
    ├── context.py
    ├── contracts.py
    ├── errors.py
    ├── registry.py
    ├── result.py
    ├── runner.py
    └── validation.py
tests/
├── fixtures/
├── integration/
└── unit/
```

## Contratos y contexto

`AgentInput` y `AgentOutput` son contratos Pydantic estrictos: rechazan campos
desconocidos, exigen contenido serializable como JSON y validan identificadores y
fechas UTC. `AgentContext` aporta identificadores de proyecto, evento, ejecución,
correlación y metadatos. Los identificadores de ejecución, evento y auditoría se
generan con UUID aleatorio; el piloto documental `PID-PILOTO-001` está admitido
explícitamente junto con el formato productivo `PID-AAAAMMDD-XXXX`.

`AgentResult` representa estados `SUCCESS`, `REQUIRES_CHANGES`, `REJECTED`,
`FAILED` y `ESCALATED`, e incluye salida, errores, advertencias, evidencias,
duración, intentos, marcas de tiempo e identificadores trazables.

## Interfaz y registro

`BaseAgent` define metadatos estables, validación de entrada, ejecución y validación
de salida. El registro es explícito: no hay descubrimiento dinámico ni importación
automática. Los duplicados se rechazan y los agentes ausentes generan un error
estructurado.

## Ejecución, errores y reintentos

`AgentRunner` crea contratos, localiza el agente, valida, ejecuta, valida la salida,
genera un resultado y persiste auditoría. El valor predeterminado permite tres
reintentos tras el intento inicial. Los errores de contrato, validación, ejecución,
escalado y timeout lógico se clasifican sin ocultar excepciones.

El timeout es lógico: detecta una ejecución que superó el límite al regresar, pero
no interrumpe por la fuerza código síncrono bloqueado.

## Auditoría y secretos

Cada resultado final se añade como JSON UTF-8 a
`AUDITORIAS/eventos/agent-events.jsonl`. El registro es append-only a nivel de
aplicación, contiene checksum SHA-256 y puede filtrarse por proyecto, agente,
ejecución y rango temporal. Las claves sensibles y patrones comunes de tokens se
sustituyen por `[REDACTED]`.

El archivo local no ofrece transacciones multiproceso ni firma criptográfica
externa. Es una base de desarrollo, no un almacén de producción.

## CLI

```powershell
.\.venv\Scripts\editorial-ia.exe list-agents
.\.venv\Scripts\editorial-ia.exe show-agent TEST-AGENT-001
.\.venv\Scripts\editorial-ia.exe run --agent TEST-AGENT-001 --project PID-PILOTO-001 --input "Prueba de infraestructura"
```

La salida es JSON. Un éxito devuelve código 0; un rechazo o error devuelve 1.

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest --cov=editorial_ia --cov-report=term-missing
```

La suite cubre contratos, identificadores, registro, validaciones, errores,
reintentos, timeout lógico, auditoría, secretos, flujo integrado y CLI.

## Extensión futura segura

Para añadir un agente en un paso posterior se deberá obtener autorización expresa,
implementar `BaseAgent`, registrarlo deliberadamente, añadir pruebas y conservar la
trazabilidad documental y de auditoría.

