# Informe del paso 9 — Infraestructura base para agentes

- **Fecha:** 2026-07-23
- **Resultado:** `COMPLETADO`
- **Alcance:** infraestructura local de desarrollo

## Resultado

Se creó un paquete Python instalable con contratos tipados, contexto, registro
explícito, runner síncrono, errores estructurados, reintentos, timeout lógico,
auditoría JSONL append-only, enmascaramiento de secretos y CLI.

Solo se implementó `TEST-AGENT-001`. Los 44 perfiles documentales permanecen como
especificaciones y no se implementó ningún agente de producción ni servicio
externo.

## Decisiones

- Python 3.12 y Pydantic 2 para contratos.
- pytest y pytest-cov para verificación.
- JSON/JSONL UTF-8 para interoperabilidad local.
- Registro explícito para evitar activaciones accidentales.
- Auditoría local con checksum y redacción preventiva.
- `ADR-0004` utilizado porque `ADR-0003` ya estaba ocupado por la votación del
  Consejo Editorial.

## Verificación

```powershell
.\.venv\Scripts\python.exe -m pytest --cov=editorial_ia --cov-report=term-missing
```

- 37 pruebas superadas.
- 0 pruebas fallidas.
- cobertura total: 91,91 %.
- umbral configurado: 85 %.

## Prueba real de CLI

```powershell
.\.venv\Scripts\editorial-ia.exe run --agent TEST-AGENT-001 --project PID-PILOTO-001 --input "Prueba de infraestructura"
```

La ejecución debe producir `SUCCESS`, devolver el texto recibido, registrar 25
caracteres y añadir una línea a `AUDITORIAS/eventos/agent-events.jsonl`.

## Limitaciones aceptadas

- ejecución local, secuencial y síncrona;
- timeout lógico sin cancelación forzosa;
- persistencia JSONL sin coordinación multiproceso;
- sin modelos de IA, APIs, base de datos, bus, web ni automatización;
- sin agentes reales de Gobierno, Operaciones o Soporte.

## Recomendación

El paso 10 debería definir y probar la máquina de estados y el contrato de
orquestación en modo local, conservando puertas humanas y sin activar agentes de
producción hasta autorización expresa.

