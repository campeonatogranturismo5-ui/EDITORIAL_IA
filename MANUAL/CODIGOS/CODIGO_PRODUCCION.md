# Código de producción

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `PENDIENTE_DE_VALIDACION`
- **Fuente:** `../../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`, secciones 8-18 y fase 4
- **Responsable de aprobación:** Responsable Técnico, Consejo Editorial y responsable humano

## Ciclo de vida

```text
IDEA
→ INVESTIGACION
→ ARQUITECTURA
→ CREACION_ASSETS
→ REDACCION
→ EDICION
→ PRODUCCION
→ PUBLICACION
→ POSTPUBLICACION
→ ARCHIVADO
```

`ARCHIVADO` se interpreta como estado terminal. La fuente denomina «nueve fases» a los estados productivos y enumera diez estados al incluirlo.

## Artefactos mínimos

| Estado | Artefactos |
|---|---|
| IDEA | `brief.md`, `viabilidad.md` |
| INVESTIGACION | `mercado.md`, `lectores.md`, `competencia.md` |
| ARQUITECTURA | `indice.md`, `ficha_capitulos.md`, `estilo.md` |
| CREACION_ASSETS | Personajes, mundo, sistemas, metáforas, ejercicios e infografías según el proyecto |
| REDACCION | `ms_capitulo_XX_vNN.md` por capítulo |
| EDICION | manuscrito editado e informe de edición |
| PRODUCCION | PDF, EPUB, audio, portada, web y recursos aplicables |
| PUBLICACION | metadatos, landing y promoción |
| POSTPUBLICACION | informe técnico a 30 días, comercial a 90 días y lecciones |

## PID y proyecto

- Identificador: `PID-AAAAMMDD-XXXX`.
- Cada proyecto mantiene `estado.json`, `log.md` y `decisiones.md`.
- Los artefactos se separan por fase y tipo.
- Nada se sobrescribe; se versiona y se conserva el historial.
- Los checkpoints deben permitir volver a un estado anterior.

## Puertas humanas

| Puerta | Alcance indicado | Decisores |
|---|---|---|
| GR-1 | Viabilidad e investigación | Humano y Consejo |
| GR-2 | Arquitectura y recursos creativos | Humano y Consejo |
| GR-3 | Manuscrito editado | Humano y Consejo |
| GR-4 | Paquetes de producción | Humano y Consejo |

La fuente sitúa GR-1 después de `INVESTIGACION` en una tabla y después de `IDEA` en los flujos. La transición definitiva queda `PENDIENTE_DE_VALIDACION`.

## Consejo Editorial

Los miembros `GOB-02a` a `GOB-02d` votan independientemente:

- `APROBAR`
- `RECHAZAR`
- `REQUIERE_CAMBIOS`

Reglas expresadas por la fuente:

- 4 aprobaciones: pasa a revisión humana.
- 3 aprobaciones: pasa con disidencia.
- 2 aprobaciones: la fuente alterna entre devolución y escalado por empate.
- 0 o 1 aprobación: devolución e incidente E5.

La consolidación de combinaciones con tres valores, especialmente 2-2, queda `PENDIENTE_DE_VALIDACION`.

## Secuencia general

1. Viabilidad.
2. Mercado, lectores y competencia en paralelo.
3. Arquitectura y estilo.
4. Recursos creativos según tipo de libro.
5. GR-2.
6. Redacción por capítulos.
7. Coherencia, estilo, corrección, hechos, originalidad, legal y paratextos.
8. GR-3.
9. Arte, formatos y materiales comerciales.
10. Auditoría y GR-4.
11. Publicación.
12. Informes postpublicación, Memoria y aprendizaje.

## Errores

- E6: desviación respecto de `../../MEMORIA/estilo_autor.md`.
- E7: ruptura de `biblia_mundo.md` o `sistemas.md`.
- E1-E5: `PENDIENTE_DE_VALIDACION`; la fuente remite a v1.0, no disponible.

## Comunicación y recuperación

Los mensajes del bus incluyen `event_id`, `timestamp`, `from_agent`, `to_agent`, `project_id`, `event_type`, `payload_ref` y `metadata`.

El comportamiento completo del bus, recuperación de proyectos, SLA y errores E1-E5 no puede migrarse porque la fuente solo indica «idéntico a v1.0».

## Estado de implementación

Todo este flujo está documentado, no implementado. La máquina de estados, el bus, los reintentos, los conectores y la publicación son `NO_IMPLEMENTADO`.

