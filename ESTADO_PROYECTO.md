# Estado del proyecto

- **Fecha:** 2026-07-23
- **Fase actual:** infraestructura base para agentes
- **Estado:** `INFRAESTRUCTURA_BASE_IMPLEMENTADA`
- **Fuente:** `DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`
- **Responsable de aprobación:** responsable humano

## Completado

- Estructura principal y subcarpetas inicializadas.
- Documento maestro incorporado.
- Inventario inicial creado.
- Marcadores documentales creados para los 44 perfiles; los seis perfiles de Gobierno fueron desarrollados posteriormente y los 38 restantes siguen pendientes.
- `AGENTS.md` raíz y ocho instrucciones locales creados.
- Jerarquía de autoridad documentada en `ADR-0001`.
- Constitución, seis Códigos enumerados, Glosario y Arquitectura del Sistema desarrollados.
- Cinco documentos de Memoria inicializados sin entradas no respaldadas.
- Informe de descomposición e índice documental creados.
- Plantilla única de agentes y seis contratos/plantillas comunes desarrollados.
- Decisión registrada en `ADR-0002`.
- Pruebas documentales de completitud definidas.
- Seis perfiles de Gobierno desarrollados conforme a la plantilla oficial.
- Votación del Consejo, matriz de consolidación y conservación de GR-1 a GR-4 definidas.
- Esquema JSON, checklist, cinco ejemplos y pruebas documentales de votación añadidos.
- Decisión de consolidación registrada en `ADR-0003`.
- Proyecto sintético `PID-PILOTO-001` creado con estado persistido `IDEA`.
- Once áreas, metadatos internos, trazabilidad y checkpoints del piloto inicializados.
- Flujo manual validado mediante 11 pruebas de integración superadas.
- Versionado sin sobrescritura y rollback por checkpoints comprobados documentalmente.
- Auditoría integral de los 17 ámbitos completada.
- Enlaces, JSON, numeración, plantilla, secretos, duplicados y estado real verificados.
- Conclusión de auditoría: `APTO_CON_CORRECCIONES`.
- Paquete Python local, contratos, contexto y registro explícito implementados.
- Runner síncrono con reintentos, timeout lógico y resultados estructurados implementado.
- Auditoría JSONL append-only con checksum y redacción de secretos implementada.
- CLI y agente sintético `TEST-AGENT-001` implementados.
- 37 pruebas automatizadas superadas con 91,91 % de cobertura.
- Decisión técnica registrada en `ADR-0004`.

## No implementado

- Contenido definitivo del Manual y la Memoria.
- Agentes ejecutables de producción; solo existe `TEST-AGENT-001`.
- Prompts.
- Máquina de estados.
- Scripts y automatizaciones.
- APIs, modelos externos, bases de datos y bus de eventos.

## Decisiones pendientes

- Incorporar el contenido heredado de v1.0.
- Confirmar 41 roles conceptuales frente a 44 perfiles ejecutables.
- Resolver la posición exacta de GR-1.
- Unificar la convención de nombres.
- Elegir la licencia.

## Próxima fase autorizable

Definir la máquina de estados y el contrato local de orquestación en un paso
posterior expresamente autorizado. La automatización real y los agentes de
producción permanecen fuera de alcance.
