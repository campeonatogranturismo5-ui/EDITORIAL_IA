# Código de seguridad

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `PENDIENTE_DE_VALIDACION`
- **Fuente:** `../../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`, principios y referencias de seguridad
- **Responsable de aprobación:** Responsable Técnico, Especialista Legal / Compliance y responsable humano

## Principio

La seguridad prevalece sobre la funcionalidad. Ninguna capacidad se activa sin control de acceso.

## Reglas definidas

- No almacenar secretos, contraseñas, claves o tokens en Git.
- Escalar riesgos legales no triviales al responsable humano.
- No conceder a un agente más herramientas o permisos que los necesarios para su misión.
- Mantener auditoría de eventos, incidentes y decisiones.
- Tratar recursos, licencias, datos de mercado y contenido de terceros conforme a sus derechos.
- Mantener separadas la documentación, los prompts, el código, los proyectos y los resultados.
- Las puertas humanas no pueden omitirse mediante automatización.

## Controles requeridos

Los siguientes controles se derivan de la arquitectura, pero todavía están `NO_IMPLEMENTADO`:

- gestión de identidades y permisos por agente;
- almacén de secretos;
- cifrado y retención de datos;
- registro inmutable;
- backups y recuperación;
- clasificación de datos;
- gestión de incidentes;
- validación de proveedores y licencias;
- revisión de privacidad;
- protección contra publicación accidental.

## Dependencia ausente

La fuente no contiene el detalle de accesos, datos o *compliance* y no aporta el Código de Seguridad v1.0. No se añaden políticas externas para evitar convertir una propuesta en norma aprobada.

