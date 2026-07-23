# PID-PILOTO-001 — Proyecto piloto documental

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado actual:** `IDEA`
- **Naturaleza:** `SIMULACION_NO_PUBLICABLE`
- **Fuente:** paso 7 autorizado y `../../../MANUAL/CODIGOS/CODIGO_PRODUCCION.md`
- **Responsable de aprobación:** responsable humano

## Finalidad

Comprobar manualmente la estructura, las transiciones, los artefactos obligatorios, las puertas humanas, los rechazos, los reintentos, la auditoría, el versionado y los checkpoints.

`PID-PILOTO-001` es el identificador sintético exigido para esta prueba y constituye una excepción explícita al formato general `PID-AAAAMMDD-XXXX`.

## Advertencia

Todo el contenido es ficticio, mínimo y deliberadamente no publicable. No representa un libro real, una decisión editorial real ni una ejecución automática.

## Estructura

- `_meta/`: estado interno y configuración documental.
- `brief/`: idea y brief mínimo.
- `investigacion/`: viabilidad, mercado, lectores y competencia.
- `arquitectura/`: índice, capítulos y estilo.
- `assets_creativos/`: manifiesto de recursos simulados.
- `manuscrito/`: dos versiones mínimas para comprobar no sobrescritura.
- `edicion/`: manuscrito editado e informe.
- `produccion/`: manifiesto de paquete.
- `publicacion/`: metadatos, landing y promoción simuladas.
- `postpublicacion/`: informes y lecciones simulados.
- `checkpoints/`: snapshots documentales para retorno.
- `log.md`, `decisiones.md` y `riesgos.md`: trazabilidad.

## Reglas

1. El estado persistido permanece en `IDEA`.
2. Las transiciones del piloto se ejecutan solo en memoria dentro de `TEST/integracion/proyecto-piloto/`.
3. GR-1 a GR-4 nunca se consideran aprobadas sin referencia humana.
4. La posición exacta de GR-1 sigue pendiente; el piloto no la resuelve.
5. Ningún archivo versionado se sobrescribe.
6. No existe automatización, publicación, modelo de IA ni bus de eventos.
