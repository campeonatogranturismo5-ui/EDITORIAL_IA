# Auditoría de la fase inicial de Editorial IA

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Alcance:** repositorio completo hasta el paso 7
- **Tipo:** auditoría documental y técnica local, sin servicios externos
- **Responsable de revisión:** Codex
- **Responsable de aprobación:** responsable humano

## Resumen ejecutivo

La base documental es coherente, trazable y reproducible para continuar con fases documentales controladas. No está preparada para automatización real, publicación ni operación con agentes ejecutables.

Se revisaron 221 archivos versionados, 44 perfiles de agente, los documentos de autoridad, tres ADR, cinco ejemplos de votación, el piloto `PID-PILOTO-001` y sus pruebas. No se encontraron secretos, enlaces rotos, JSON inválidos, identificadores duplicados, archivos no vacíos con contenido idéntico ni afirmaciones falsas de implementación.

Durante la auditoría se corrigieron dos inconsistencias documentales menores:

1. `MANUAL/CODIGOS/CODIGO_PRODUCCION.md` seguía presentando la consolidación de votos como pendiente pese a la resolución documental de `ADR-0003`.
2. `ESTADO_PROYECTO.md` describía las 44 fichas como marcadores pendientes sin distinguir los seis perfiles de Gobierno ya desarrollados.

No se aplicó ninguna decisión arquitectónica nueva.

## Método y evidencias

- Inventario mediante Git y recorrido completo del árbol.
- Validación de enlaces Markdown relativos.
- Análisis de identificadores y numeración de agentes.
- Comparación de las 33 secciones de plantilla y fichas de Gobierno.
- Parseo de todos los JSON.
- Validación de cinco fixtures contra el esquema de votación.
- Búsqueda de patrones de secretos y credenciales.
- Detección SHA-256 de duplicados exactos no vacíos.
- Ejecución de las pruebas del Consejo y del piloto.
- Verificación de integridad Git mediante `git fsck --no-dangling`.

## Resultado por punto auditado

| Nº | Área | Resultado | Evidencia principal |
|---:|---|---|---|
| 1 | Arquitectura v2.0 frente al repositorio | conforme con pendientes explícitos | Constitución, Códigos, Arquitectura e inventario |
| 2 | Jerarquía documental | conforme | `AGENTS.md` y `ADR-0001` |
| 3 | Cumplimiento de `AGENTS.md` | conforme | trazabilidad, límites y una fase por commit |
| 4 | Enlaces relativos | conforme | 0 enlaces rotos |
| 5 | Nombres de carpetas y archivos | conforme con convención pendiente | 0 colisiones; nombres canónicos preservados |
| 6 | Numeración de agentes | conforme | 41 números conceptuales, 44 perfiles únicos |
| 7 | Estados de implementación | conforme | diseño, simulación y no implementación separados |
| 8 | Plantilla común | conforme | 33/33 secciones, sin ausencias ni duplicados |
| 9 | Puertas humanas | conforme | GR-1 a GR-4 siempre obligatorias |
| 10 | Votación | conforme para simulación | esquema, `ADR-0003`, checklist y 5 fixtures |
| 11 | Trazabilidad | conforme | ADR, changelog, estado, logs e informes |
| 12 | Versionado | conforme documentalmente | Git, `_v01/_v02` y checkpoints |
| 13 | Secretos | conforme | 0 coincidencias |
| 14 | Archivos duplicados | conforme | 0 duplicados exactos no vacíos |
| 15 | Falsas afirmaciones de implementación | conforme | capacidades técnicas marcadas `NO_IMPLEMENTADO` |
| 16 | Pruebas del piloto | conforme | 11/11 superadas |
| 17 | Estado real | coherente | base documental definida; automatización ausente |

Los 67 archivos `.gitkeep` vacíos son marcadores intencionales de directorio y no se consideran duplicados documentales.

## Hallazgos críticos

Ninguno.

## Hallazgos altos

Ninguno.

## Hallazgos medios

### MED-001 — Posición de GR-1 sin resolver

La fuente sitúa GR-1 después de `IDEA` y también después de `INVESTIGACION`. El piloto evita decidirlo. Debe existir aprobación humana y ADR antes de implementar la transición.

### MED-002 — Máquina de estados y workflows no implementados

`WORKFLOWS/maquinas_estado/proyecto.json` sigue siendo un marcador `PENDIENTE`; los flujos son documentos pendientes. No existe motor, persistencia, bloqueo, idempotencia ni rollback real.

### MED-003 — Gobierno operativo incompleto

Solo seis perfiles de Gobierno tienen ficha completa. Los otros 38 perfiles son marcadores, y ningún agente es ejecutable.

### MED-004 — Recuperación, SLA y E1–E5 incompletos

La arquitectura remite a v1.0, que no está disponible. No deben implementarse reintentos o incidentes reales hasta recuperar o sustituir esa fuente mediante decisión aprobada.

### MED-005 — Independencia de voto verificable solo documentalmente

Los fixtures declaran `sealed: true` y `saw_other_votes: false`, pero no existe aislamiento técnico, almacenamiento inmutable ni control temporal. La prueba demuestra coherencia del registro, no independencia operativa real.

### MED-006 — Controles de seguridad no implementados

No existen autenticación, autorización, gestión de secretos, registros inmutables ni conectores controlados. Esto impide habilitar automatización o servicios externos.

### MED-007 — Licencia pendiente

`LICENSE.md` no establece una licencia. Debe resolverse antes de distribución, reutilización externa o publicación de contenido.

## Hallazgos bajos

### BAJ-001 — Convención de nombres no unificada

Coexisten nombres canónicos en mayúsculas y guiones bajos con la preferencia general por `kebab-case`. La contradicción ya está registrada y no causa colisiones.

### BAJ-002 — `CODEOWNERS` pendiente

El archivo existe como marcador sin responsables efectivos. Es coherente con el estado actual, pero deberá completarse antes de un flujo de revisión real.

### BAJ-003 — Identificador sintético fuera del patrón general

`PID-PILOTO-001` no cumple `PID-AAAAMMDD-XXXX`, pero fue exigido expresamente por el paso 7 y está documentado como excepción no productiva.

## Recomendaciones

1. Resolver GR-1 mediante aprobación humana y una ADR.
2. Recuperar v1.0 o aprobar sustituciones explícitas para E1–E5, recuperación y SLA.
3. Definir y validar una máquina de estados declarativa antes de programar un motor.
4. Diseñar aislamiento de votos, sellado inmutable y auditoría verificable.
5. Completar seguridad, permisos, secretos y rollback antes de conectar servicios.
6. Elegir licencia y responsables de `CODEOWNERS`.
7. Decidir mediante ADR la convención de nombres y la relación 41 roles/44 perfiles.
8. Mantener prohibida la automatización hasta superar una auditoría técnica específica.

## Pruebas ejecutadas

| Prueba | Resultado |
|---|---|
| estructura de plantilla | 33/33, superada |
| fichas de Gobierno | 6 × 33 secciones, superada |
| votación del Consejo | 5/5 fixtures, superada |
| integración del piloto | 11/11, superada |
| JSON | todos válidos |
| enlaces | 0 rotos |
| secretos | 0 coincidencias |
| duplicados no vacíos | 0 grupos |
| numeración | 44 perfiles únicos; números 01–41 presentes |
| integridad Git | superada |

## Estado real del sistema

### Definido documentalmente

- Constitución, Códigos, Arquitectura y jerarquía.
- Plantilla y contratos comunes.
- Seis perfiles de Gobierno.
- Votación para simulación documental.
- Proyecto piloto sintético y pruebas locales.

### Pendiente o no implementado

- 38 fichas completas restantes y los 44 agentes ejecutables.
- Prompts operativos.
- Máquina de estados, bus de eventos y automatizaciones.
- Persistencia, APIs, modelos externos y bases de datos.
- Publicación, métricas reales, Memoria aprendida y controles de seguridad.

## Conclusión

`APTO_CON_CORRECCIONES`

La conclusión autoriza únicamente continuar con trabajo documental expresamente aprobado. No autoriza automatización, conexión de IA, uso de servicios externos ni publicación.
