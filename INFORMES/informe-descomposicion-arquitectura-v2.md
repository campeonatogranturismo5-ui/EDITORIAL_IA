# Informe de descomposición de la arquitectura v2.0

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`
- **Responsable de aprobación:** responsable humano

## Resultado

El documento maestro se ha distribuido en documentación Markdown mantenible. La migración preserva reglas, estados y terminología; no crea agentes ejecutables, prompts ni automatizaciones.

## Contenido migrado

- Misión, visión, catorce principios y objetivos.
- Convenciones editoriales por tipo de libro.
- Estándares y líneas de defensa de calidad.
- Estados, artefactos, puertas y flujo productivo.
- Seguridad disponible en la fuente y controles aún pendientes.
- Ciclo de Memoria y mejora continua.
- Objetivos, investigación y métricas comerciales.
- Capas, agentes, repositorio, comunicación e integración de Codex.
- Gobernanza de los cinco documentos de Memoria.

## Documentos generados o desarrollados

### Manual

- [Constitución](../MANUAL/CONSTITUCION.md)
- [Código de estilo](../MANUAL/CODIGOS/CODIGO_ESTILO.md)
- [Código de calidad](../MANUAL/CODIGOS/CODIGO_CALIDAD.md)
- [Código de producción](../MANUAL/CODIGOS/CODIGO_PRODUCCION.md)
- [Código de seguridad](../MANUAL/CODIGOS/CODIGO_SEGURIDAD.md)
- [Código de aprendizaje](../MANUAL/CODIGOS/CODIGO_APRENDIZAJE.md)
- [Código comercial](../MANUAL/CODIGOS/CODIGO_COMERCIAL.md)
- [Glosario](../MANUAL/GLOSARIO.md)
- [Arquitectura del sistema](../MANUAL/ARQUITECTURA_SISTEMA.md)

### Memoria

- [Decisiones editoriales](../MEMORIA/decisiones_editoriales.md)
- [Errores históricos](../MEMORIA/errores_historicos.md)
- [Mejores prácticas](../MEMORIA/mejores_practicas.md)
- [Estilo del autor](../MEMORIA/estilo_autor.md)
- [Conocimientos acumulados](../MEMORIA/conocimientos_acumulados.md)

## Contenido pendiente

- E1-E5.
- Recuperación de proyectos.
- Detalle completo del control de versiones.
- Gobernanza heredada no reproducida en v2.0.
- SLA completos.
- Anexo de ficción del Código de Estilo.
- Fórmula del ICE.
- Matriz completa de votación.
- Contratos del bus de eventos.
- Código de Seguridad detallado.

La causa común es que el maestro dice «idéntico a v1.0», pero la arquitectura v1.0 no está disponible en `DOCUMENTACION_FUENTE/`.

## Contradicciones

1. GR-1 figura después de investigación y también después de idea.
2. Un resultado 2-2 se devuelve o se escala según la sección.
3. La capa editorial se rotula como 18 agentes, pero contiene 19.
4. Existen 41 roles conceptuales y 44 perfiles al desglosar el Consejo.
5. La convención `kebab-case` contradice varios nombres canónicos.
6. Registro de decisiones aparece como archivo y como directorio.
7. Memoria aparece como `MEMORIA_EDITORIAL/` y como `MEMORIA/`.
8. El cierre habla de nueve fases y la máquina enumera diez estados con `ARCHIVADO`.
9. `informe_comercial.md` e `informe_comercial_90d.md` no están unificados.
10. Las APIs y métricas comerciales no tienen contrato de disponibilidad.
11. El cierre declara siete Códigos, pero la estructura y el PASO 4 enumeran seis.

No se ha resuelto ninguna contradicción mediante una decisión inventada.

## Decisiones humanas requeridas

- Incorporar v1.0 o declarar obsoleto su contenido.
- Determinar la posición de GR-1.
- Aprobar una tabla de consolidación de votos.
- Confirmar la taxonomía 41 roles / 44 perfiles.
- Aprobar la convención de nombres.
- Definir ICE y fuentes de métricas.
- Definir seguridad, proveedores y publicación.

## Estados aplicados

- `DEFINIDO`: regla explícita y trasladada fielmente.
- `BORRADOR`: contenido organizado pero sujeto a ampliación o validación.
- `PENDIENTE_DE_VALIDACION`: existe una contradicción, dependencia o criterio ausente.
- `NO_IMPLEMENTADO`: capacidad diseñada sin ejecución técnica o sin evidencia.

## Enlaces y trazabilidad

Todos los documentos incluyen versión, fecha, estado, fuente y responsable de aprobación. Los enlaces relativos fueron diseñados para conectar Constitución, Códigos, Memoria, arquitectura e informe.

## Limitación

La fuente DOCX no se ha modificado. Esta fase es una descomposición documental, no una certificación de que el sistema esté implementado.
