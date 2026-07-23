# Casos de integración — PID-PILOTO-001

- **Versión:** `1.0`
- **Fecha:** `2026-07-23`
- **Estado:** `DEFINIDO`
- **Ejecución:** local, documental y sin mutaciones

| ID | Comprobación | Resultado esperado |
|---|---|---|
| PIL-001 | estructura completa | ningún directorio ausente |
| PIL-002 | estado inicial | `IDEA`, simulado y no publicable |
| PIL-003 | artefactos obligatorios | todas las rutas declaradas existen |
| PIL-004 | avance de estado | avanza con artefactos; bloquea sin ellos |
| PIL-005 | puerta humana | GR-2 bloquea sin aprobación |
| PIL-006 | rechazo | GR-2 devuelve a `ARQUITECTURA` |
| PIL-007 | reintentos | el tercero escala |
| PIL-008 | auditoría | cada acción documental está en el log |
| PIL-009 | no sobrescritura | v01 y v02 coexisten y difieren |
| PIL-010 | rollback | checkpoint posterior referencia CP-000 |
| PIL-011 | ausencia de mutación | el estado persistido sigue en `IDEA` |

GR-1 no se usa para probar rechazo porque su posición sigue `PENDIENTE_DE_VALIDACION`.

## Ejecución

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\TEST\integracion\proyecto-piloto\validar-piloto.ps1
```
