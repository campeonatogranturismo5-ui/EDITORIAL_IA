# Código de aprendizaje

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`, secciones 18-19 y fase 5
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Principio

Cada libro es un experimento. Produce datos técnicos y comerciales; los datos alimentan la Memoria y la Memoria mejora el sistema.

## Ciclo

1. `SUP-38` produce un informe técnico a 30 días.
2. `SUP-39` produce un informe comercial a 90 días.
3. `SUP-40` reúne informes, auditorías, votos y feedback humano.
4. El Curador propone entradas con evidencia.
5. El Consejo aprueba decisiones editoriales y preferencias del autor.
6. Las mejores prácticas y errores pueden autoaprobarse con evidencia de al menos dos libros.
7. El conocimiento de nicho requiere al menos tres libros del mismo nicho.
8. `SUP-41` propone cambios de prompts, reglas o Códigos.
9. El Consejo aprueba cambios de Código.
10. El Gestor de Versiones aplica cambios autorizados.
11. Las pruebas de regresión deciden entre integración y rollback.

## Memoria

- [Decisiones editoriales](../../MEMORIA/decisiones_editoriales.md).
- [Errores históricos](../../MEMORIA/errores_historicos.md).
- [Mejores prácticas](../../MEMORIA/mejores_practicas.md).
- [Estilo del autor](../../MEMORIA/estilo_autor.md).
- [Conocimientos acumulados](../../MEMORIA/conocimientos_acumulados.md).

## Reglas de evidencia

- Ninguna entrada se inventa.
- Una lección de un solo libro no se generaliza.
- `estilo_autor.md` solo cambia con evidencia explícita del autor.
- El Curador propone; no cambia la Constitución.
- El Agente de Aprendizaje propone; no aplica cambios.
- Los cambios deben quedar versionados y auditados.

## Métricas

- Reducción de errores en categorías tratadas.
- Libros necesarios para estabilizar un agente.
- Evolución del ICE medio.
- Evolución de KPI comerciales.
- Satisfacción del autor igual o superior a 8/10.
- Citas de la Memoria en al menos el 60 % de las decisiones.

## Antipatrones

- Cambiar un prompt por evidencia de un solo libro.
- Olvidar preferencias explícitas del autor.
- Consejo monocorde: correlación superior a 0,9 durante cinco libros.
- Memoria ignorada: citas inferiores al 40 % durante tres libros.

## Estado técnico

El ciclo está `DEFINIDO` documentalmente. La extracción de datos, actualización automática, pruebas y rollback están `NO_IMPLEMENTADO`.

