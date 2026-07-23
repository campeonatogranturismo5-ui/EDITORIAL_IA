# Glosario

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `BORRADOR`
- **Fuente:** `../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Términos

**ADR**
Registro de una decisión de arquitectura, su contexto y consecuencias.

**Agente**
Rol especializado con misión, entradas, proceso, salidas, prohibiciones y criterios de aceptación.

**Agente ejecutable**
Implementación técnica de un perfil de agente. Las fichas Markdown no constituyen por sí mismas una implementación.

**Assets creativos**
Personajes, mundo, sistemas, metáforas, ejercicios e infografías preparados antes de redactar.

**Auditoría**
Evidencia independiente sobre eventos, decisiones, calidad, incidentes o votaciones.

**Bus de eventos**
Mecanismo diseñado para comunicar agentes mediante mensajes estructurados. Estado actual: `NO_IMPLEMENTADO`.

**Checkpoint**
Punto versionado que permite regresar a un estado anterior.

**Código**
Norma que desarrolla la Constitución y puede evolucionar con la gobernanza aprobada.

**Consejo Editorial**
Órgano colegiado compuesto por Director Editorial, Marketing, Calidad y Técnico.

**Codex**
Sistema operativo del proyecto: lee instrucciones y ejecuta acciones autorizadas; no decide política editorial o comercial.

**CREACION_ASSETS**
Estado situado entre arquitectura y redacción para preparar recursos creativos.

**E6 — Error de voz**
Desviación respecto de una preferencia válida de `../MEMORIA/estilo_autor.md`.

**E7 — Error de consistencia de mundo**
Ruptura de una regla documentada en la biblia de mundo o de sistemas.

**Gate Review (GR)**
Puerta de revisión que combina evaluación colegiada y aprobación humana.

**ICE**
Índice de Calidad Editorial. Sus umbrales están definidos; su fórmula está `PENDIENTE_DE_VALIDACION`.

**Memoria Editorial**
Conocimiento persistente formado por decisiones, errores, prácticas, estilo del autor y conocimiento de nicho.

**PID**
Identificador de proyecto con formato `PID-AAAAMMDD-XXXX`.

**Prompt**
Instrucción versionada que implementará el comportamiento de un agente. Estado actual: `NO_IMPLEMENTADO`.

**Rol conceptual**
Posición numerada en la arquitectura. Hay 41 roles conceptuales.

**Perfil de agente**
Ficha individual potencialmente ejecutable. Al desglosar el Consejo existen 44 perfiles.

**Trazabilidad**
Capacidad de relacionar cada decisión, cambio y salida con fuentes y eventos.

**Voto colegiado**
Resultado individual `APROBAR`, `RECHAZAR` o `REQUIERE_CAMBIOS`, emitido sin conocer los otros votos.

## Pendientes terminológicos

- Unificar «Memoria Editorial», `MEMORIA_EDITORIAL/` y `MEMORIA/`.
- Unificar «interfaz humano» e «interfaz humana».
- Determinar si «agente» designa roles conceptuales o perfiles ejecutables.
- Formalizar «fase», «estado» y estado terminal `ARCHIVADO`.
