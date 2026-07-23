# Informe de prueba — PID-PILOTO-001

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado:** `SUPERADA`
- **Naturaleza:** prueba documental, sintética y no publicable
- **Responsable de aprobación:** responsable humano

## Pruebas superadas

1. La estructura contiene las once áreas exigidas.
2. El estado inicial y persistido es `IDEA`.
3. Cada estado declara artefactos obligatorios y todas las rutas fixture existen.
4. Una transición simulada avanza con artefactos y se bloquea sin ellos.
5. GR-2 no puede saltarse sin aprobación humana.
6. Un rechazo en GR-2 devuelve a `ARQUITECTURA`.
7. El tercer reintento produce `ESCALADO`.
8. Las acciones documentales quedan registradas en `log.md`.
9. Las versiones v01 y v02 coexisten y difieren.
10. Un checkpoint posterior declara retorno a `CP-000`.
11. La prueba no muta `_meta/estado.json`.

Resultado reproducible: `11/11`.

## Pruebas fallidas

Ninguna.

## Limitaciones

- La posición de GR-1 sigue `PENDIENTE_DE_VALIDACION`; no se eligió implícitamente.
- El identificador `PID-PILOTO-001` es una excepción sintética ordenada por el paso 7.
- Los artefactos prueban presencia y versionado, no calidad editorial.
- E1-E5 no están completamente definidos por falta de la fuente v1.0.
- No se validan tiempos, concurrencia, permisos reales, persistencia externa ni recuperación ante fallos.

## Partes todavía simuladas

- Transiciones de estado y devoluciones.
- Aprobaciones humanas y votaciones.
- Reintentos y escalado.
- Creación y restauración de checkpoints.
- Manuscrito, edición, producción, publicación y postpublicación.
- Logs y metadatos como registros documentales.

## Requisitos para la automatización real

1. Resolver y aprobar la posición de GR-1.
2. Definir una máquina de estados versionada con precondiciones y rollback.
3. Implementar persistencia atómica, bloqueo e idempotencia.
4. Implementar autenticación, autorización y almacenamiento seguro.
5. Definir el bus de eventos, reintentos, cola fallida y recuperación.
6. Integrar la interfaz humana para GR-1 a GR-4.
7. Validar contratos y esquemas automáticamente.
8. Añadir pruebas de concurrencia, fallo, seguridad y regresión.
9. Aprobar clasificación E1-E5 y SLA.
10. Mantener versionado inmutable de artefactos y checkpoints.

## Evidencias

- Proyecto: `../LIBROS/activos/PID-PILOTO-001/`.
- Casos: `../TEST/integracion/proyecto-piloto/casos.md`.
- Resultado: `../TEST/integracion/proyecto-piloto/RESULTADOS.md`.
- Prueba: `../TEST/integracion/proyecto-piloto/validar-piloto.ps1`.

No se implementó automatización real ni se avanzó a otra fase.
