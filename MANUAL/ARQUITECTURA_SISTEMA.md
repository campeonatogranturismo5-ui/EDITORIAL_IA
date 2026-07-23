# Arquitectura del sistema

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `PENDIENTE_DE_VALIDACION`
- **Fuente:** `../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`, fases 2-5 e integración Codex
- **Responsable de aprobación:** Consejo Editorial, Responsable Técnico y responsable humano

## Alcance

Editorial IA se diseña como un sistema documental, editorial y técnico capaz de operar durante diez años. La arquitectura está definida; la automatización permanece `NO_IMPLEMENTADO`.

## Componentes

1. [Constitución](CONSTITUCION.md) y [Códigos](CODIGOS/).
2. [Memoria Editorial](../MEMORIA/).
3. Fichas de agentes en `../AGENTS/`.
4. Prompts versionados en `../PROMPTS/`.
5. Flujos y máquina de estados en `../WORKFLOWS/`.
6. Proyectos en `../LIBROS/`.
7. Auditorías e informes.
8. Scripts, automatizaciones y CI futuros.

## Capas de agentes

| Capa | Numeración | Roles declarados | Recuento real |
|---|---|---:|---:|
| Gobierno | GOB-01 a GOB-03 | 3 | 3 roles / 6 perfiles |
| Creativa | OPS-04 a OPS-09 | 6 | 6 |
| Editorial | OPS-10 a OPS-28 | 18 | 19 |
| Comercial | OPS-29 a OPS-33 | 5 | 5 |
| Soporte | SUP-34 a SUP-41 | 8 | 8 |

Hay 41 roles conceptuales. Al sustituir el rol compuesto `GOB-02` por cuatro miembros independientes se obtienen 44 perfiles.

## Catálogo de roles

| ID | Rol | Misión resumida |
|---|---|---|
| GOB-01 | Orquestador Maestro | Coordinar estados, tareas, reintentos, votaciones y escalados |
| GOB-02 | Consejo Editorial | Resolver colegiadamente las puertas editoriales |
| GOB-03 | Auditor de Calidad | Medir de forma independiente e informar desviaciones |
| OPS-04 | Diseñador de Personajes | Crear personajes, arcos, voces y relaciones |
| OPS-05 | Constructor de Mundos | Definir mundo, culturas, geografía y reglas |
| OPS-06 | Diseñador de Sistemas | Formalizar magia, tecnología, economía o política |
| OPS-07 | Diseñador de Metáforas | Construir metáforas coherentes para todo el libro |
| OPS-08 | Diseñador de Ejercicios | Crear ejercicios graduados con solución |
| OPS-09 | Especialista en Infografías | Especificar diagramas y recursos visuales didácticos |
| OPS-10 | Analista de Viabilidad | Informar si la idea merece evaluación humana |
| OPS-11 | Investigador de Mercado | Cuantificar audiencia y tendencias con fuentes |
| OPS-12 | Analista de Lectores | Definir arquetipos, dolores, deseos y objeciones |
| OPS-13 | Analista de Competencia | Analizar competidores y huecos con evidencia |
| OPS-14 | Arquitecto de Contenido | Diseñar índice, capítulos y arco |
| OPS-15 | Diseñador de Estilo | Especializar voz, tono y convenciones |
| OPS-16 | Escritor de No-Ficción | Redactar capítulos factuales y aplicables |
| OPS-17 | Escritor de Ficción | Redactar respetando personajes, mundo y sistemas |
| OPS-18 | Escritor de Paratextos | Crear prólogos, epílogos, biografía y contraportada |
| OPS-19 | Editor de Estilo | Mejorar fluidez sin cambiar ideas |
| OPS-20 | Corrector Ortotipográfico | Eliminar errores lingüísticos y tipográficos |
| OPS-21 | Verificador de Hechos | Clasificar afirmaciones como validadas, no verificadas o falsas |
| OPS-22 | Verificador de Coherencia | Detectar contradicciones internas |
| OPS-23 | Verificador de Originalidad | Detectar plagio y similitudes excesivas |
| OPS-24 | Especialista Legal / Compliance | Detectar y escalar riesgos legales |
| OPS-25 | Director de Arte | Definir portada, paleta, tipografía e ilustración |
| OPS-26 | Ilustrador | Producir imágenes según briefs aprobados |
| OPS-27 | Maquetador PDF | Crear PDF profesional y validado |
| OPS-28 | Maquetador EPUB | Crear EPUB válido y accesible |
| OPS-29 | Productor de Audiolibro | Crear audio por capítulos y validar pronunciación |
| OPS-30 | Copywriter Editorial | Crear descripción, contraportada y textos comerciales |
| OPS-31 | Especialista SEO / Keywords | Definir palabras clave y categorías |
| OPS-32 | Diseñador Web | Crear landing accesible y *mobile-first* |
| OPS-33 | Estratega Promocional | Adaptar contenido a plataformas |
| SUP-34 | Gestor de Assets | Almacenar, indexar y comprobar integridad |
| SUP-35 | Gestor de Versiones | Aplicar versionado, ramas y commits |
| SUP-36 | Registrador de Auditoría | Persistir eventos en un registro inmutable |
| SUP-37 | Notificador / Interfaz Humana | Presentar puertas y votos al humano |
| SUP-38 | Analista Post-Publicación Técnico | Producir métricas técnicas a 30 días |
| SUP-39 | Analista de Métricas Comerciales | Producir KPI comerciales a 90 días |
| SUP-40 | Curador de Memoria | Extraer patrones y proponer entradas |
| SUP-41 | Agente de Aprendizaje | Proponer mejoras respaldadas por evidencia |

El Consejo se materializa en `GOB-02a` Director Editorial, `GOB-02b` Marketing, `GOB-02c` Calidad y `GOB-02d` Técnico. Sus fichas están definidas documentalmente en `../AGENTS/GOB/` y permanecen `NO_IMPLEMENTADO` técnicamente.

## Gobierno

- `GOB-01` mantiene estado, despacha tareas, gestiona reintentos y convoca votaciones.
- `GOB-02a-d` evalúan catálogo, mercado, calidad y técnica.
- `GOB-03` audita una muestra aleatoria reproducible del 20 %; solo calculará el ICE cuando exista una fórmula aprobada.
- GR-1 a GR-4 conservan aprobación humana.
- La votación independiente y su consolidación se definen en `REGISTRO_DECISIONES/ADR-0003-votacion-consejo-editorial.md`.

## Operación

- Investigación: viabilidad, mercado, lectores y competencia.
- Arquitectura: índice, capítulos y estilo.
- Recursos: personajes, mundo, sistemas, metáforas, ejercicios e infografías.
- Redacción: ficción, no ficción y paratextos.
- Edición: estilo, corrección, hechos, coherencia, originalidad y legal.
- Producción: arte, ilustración, PDF, EPUB, audio y web.
- Comercial: copy, SEO y promoción.
- Soporte: assets, versiones, auditoría, interfaz humana, métricas, Memoria y aprendizaje.

## Comunicación

El bus propuesto transmite:

```json
{
  "event_id": "PENDIENTE",
  "timestamp": "PENDIENTE",
  "from_agent": "PENDIENTE",
  "to_agent": "PENDIENTE",
  "project_id": "PID-AAAAMMDD-XXXX",
  "event_type": "PENDIENTE",
  "payload_ref": "PENDIENTE",
  "metadata": {}
}
```

Persistencia, orden, idempotencia, reintentos, eventos fallidos y seguridad no están especificados.

## Repositorio

Las áreas principales son `MANUAL/`, `MEMORIA/`, `AGENTS/`, `REGLAS/`, `PROMPTS/`, `WORKFLOWS/`, `CHECKLISTS/`, `PLANTILLAS/`, `LIBROS/`, `INFORMES/`, `AUDITORIAS/`, `TEST/`, `SCRIPTS/`, `AUTOMATIZACIONES/`, `RECURSOS/`, `IMAGENES/`, `PORTADAS/` y `.github/`.

`DOCUMENTACION_FUENTE/` y `ESTADO_PROYECTO.md` se incorporaron en la fase inicial para trazabilidad.

## Codex

Codex está destinado a:

- crear estructura y proyectos;
- leer Manual, agentes y Memoria;
- ejecutar prompts autorizados;
- escribir artefactos y estados;
- mantener Git y auditorías;
- ejecutar comprobaciones.

Codex no toma decisiones editoriales ni comerciales.

## Automatización diseñada

- Crear PID y estado.
- Despachar tareas en paralelo.
- Validar condiciones de entrada y salida.
- Convocar Consejo y puertas humanas.
- Ejecutar producción y publicación.
- Programar informes a 30 y 90 días.
- Actualizar Memoria y proponer mejoras.
- Ejecutar regresión y rollback.

Todas estas capacidades están `NO_IMPLEMENTADO`.

## Contradicciones que requieren decisión

1. GR-1 después de `IDEA` o después de `INVESTIGACION`.
2. Capa editorial declarada como 18 aunque contiene 19 roles.
3. 41 roles frente a 44 perfiles.
4. `kebab-case` frente a nombres canónicos en mayúsculas y guiones bajos.
5. `REGISTRO_DECISIONES.md` frente a directorio de ADR.
6. `MEMORIA_EDITORIAL/` frente a `MEMORIA/`.
7. Diez estados frente a nueve fases.
8. Fórmula del ICE ausente.
9. Contenido E1-E5, recuperación, versionado y gobernanza remitido a v1.0 no disponible.

La devolución y el escalado en 2-2, junto con la matriz completa de consolidación, quedaron resueltos para simulación documental mediante `ADR-0003`.
12. APIs comerciales y permisos no validados.
13. El documento declara siete Códigos, pero solo enumera seis archivos de Código.

## Dependencias técnicas futuras

- Proveedores de modelos de lenguaje, imagen y voz.
- Base de datos y almacenamiento de objetos.
- Cola o bus de eventos.
- Gestión de secretos.
- APIs de publicación y métricas.
- Validadores PDF, EPUB y accesibilidad.
- Detección de similitud y verificación factual.
- Observabilidad, backups y recuperación.

## Documentos relacionados

- [Código de producción](CODIGOS/CODIGO_PRODUCCION.md)
- [Código de seguridad](CODIGOS/CODIGO_SEGURIDAD.md)
- [Código de aprendizaje](CODIGOS/CODIGO_APRENDIZAJE.md)
- [Glosario](GLOSARIO.md)
- [ADR-0001](REGISTRO_DECISIONES/ADR-0001-jerarquia-instrucciones.md)
