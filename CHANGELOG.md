# Registro de cambios

## 2026-07-23 — Infraestructura base para agentes

- Creado el paquete Python `editorial_ia` con contratos Pydantic y contexto trazable.
- Añadidos registro explícito, runner síncrono, reintentos, timeout lógico y errores estructurados.
- Añadida auditoría JSONL append-only con checksum y enmascaramiento de secretos.
- Añadida CLI y el único agente ejecutable `TEST-AGENT-001`.
- Añadidas 37 pruebas automatizadas; todas superadas con 91,91 % de cobertura.
- Registrada la decisión técnica en `ADR-0004`.
- No se implementaron agentes de producción ni integraciones externas.

## 2026-07-23 — Auditoría integral de la base inicial

- Auditados 221 archivos versionados y los 17 ámbitos exigidos por el paso 8.
- Verificados enlaces, nombres, numeración, estados, plantilla, puertas humanas, votación, trazabilidad, versionado, secretos, duplicados y piloto.
- Corregidas dos inconsistencias documentales menores sin cambiar arquitectura.
- Pruebas superadas: plantilla 33/33, Consejo 5/5 y piloto 11/11.
- Emitida la conclusión `APTO_CON_CORRECCIONES`.
- No se implementaron funciones ni fases posteriores.

## 2026-07-23 — Proyecto piloto documental

- Creado `PID-PILOTO-001` con estado persistido `IDEA`.
- Añadidas las once áreas del expediente, metadatos, log, decisiones, riesgos y checkpoints.
- Creados artefactos sintéticos mínimos y versiones coexistentes sin contenido publicable.
- Añadidas once pruebas de integración para transiciones, artefactos, puertas humanas, rechazo, reintentos, auditoría, versionado y rollback.
- Resultado de integración: 11 pruebas superadas y 0 fallidas.
- No se implementó automatización real, publicación, modelo de IA ni bus de eventos.

## 2026-07-23 — Capa documental de Gobierno

- Desarrolladas las fichas completas de `GOB-01`, `GOB-02a` a `GOB-02d` y `GOB-03`.
- Definida la votación independiente del Consejo con resultados `APROBAR`, `RECHAZAR` y `REQUIERE_CAMBIOS`.
- Resuelta documentalmente la consolidación 4-0, 3-1, 2-2, 1-3 y 0-4 mediante `ADR-0003`.
- Añadidos esquema JSON, checklist, cinco ejemplos sintéticos y pruebas reproducibles.
- Conservada la aprobación humana obligatoria en GR-1 a GR-4.
- No se han conectado modelos de IA ni implementado el bus de eventos.

## 2026-07-23 — Plantilla y contratos comunes

- Desarrollada la plantilla única de agentes con 33 secciones obligatorias.
- Añadidos contratos de entrada y salida.
- Añadidas plantillas de rechazo, error, decisión y checklist.
- Documentada la decisión en `ADR-0002`.
- Añadidas pruebas documentales de completitud, ausencia, duplicación, vacío, reintentos y escalado.
- No se han desarrollado las fichas de los 41 roles ni se ha implementado ningún agente.

## 2026-07-23 — Descomposición de la arquitectura v2.0

- Migrados misión, visión, principios, objetivos, normas, flujos, calidad, seguridad disponible, aprendizaje y reglas comerciales.
- Desarrollados la Constitución, los seis Códigos enumerados, el Glosario y la Arquitectura del Sistema.
- Inicializados los cinco documentos de Memoria sin inventar entradas.
- Añadidos metadatos de versión, fecha, estado, fuente y responsable.
- Añadido un índice documental al `README.md`.
- Generado `INFORMES/informe-descomposicion-arquitectura-v2.md`.
- Marcadas como pendientes las secciones que dependen de v1.0 y las contradicciones de la fuente.
- No se han desarrollado prompts, agentes ejecutables ni automatizaciones.

## 2026-07-23 — Instrucciones AGENTS para Codex

- Añadido `AGENTS.md` en la raíz con propósito, jerarquía, reglas, convenciones, comprobaciones e informe final.
- Añadidas instrucciones locales para `MANUAL/`, `MEMORIA/`, `AGENTS/`, `PROMPTS/`, `WORKFLOWS/`, `LIBROS/`, `TEST/` y `AUTOMATIZACIONES/`.
- Registrada la jerarquía de instrucciones en `MANUAL/REGISTRO_DECISIONES/ADR-0001-jerarquia-instrucciones.md`.
- No se han creado agentes ejecutables ni se ha avanzado a la descomposición del documento maestro.

## 2026-07-23 — Estructura inicial

- Creada la estructura inicial del repositorio.
- Incorporado el documento maestro de arquitectura v2.0.
- Inicializados Manual, Memoria, agentes, reglas, prompts, workflows, plantillas, libros, informes, auditorías, pruebas, scripts, automatizaciones y recursos.
- Creadas fichas documentales pendientes para los 41 roles numerados; el Consejo Editorial se representa mediante cuatro perfiles `GOB-02a` a `GOB-02d`.
- Añadido el inventario inicial y el estado del proyecto.
- No se ha implementado lógica, agentes ejecutables ni integración externa.
