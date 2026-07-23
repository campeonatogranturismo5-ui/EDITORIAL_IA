# Pruebas documentales del Consejo Editorial

- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Alcance:** simulación local sin IA, red ni bus de eventos

## Ejecución

Desde la raíz del repositorio:

```powershell
& ./TEST/unitarios/consejo-editorial/validar-votaciones.ps1
```

La prueba comprueba:

- presencia exacta de los cuatro miembros;
- independencia (`sealed: true`, `saw_other_votes: false`);
- justificación no vacía;
- al menos una referencia normativa;
- consolidación 4-0, 3-1, 2-2, 1-3 y 0-4;
- permanencia de la aprobación humana en GR-1 a GR-4.

Los cinco JSON son ejemplos sintéticos, no registros de decisiones reales.

## Última ejecución

- **Fecha:** 2026-07-23
- **Resultado:** `SUPERADA`
- **Ejemplos validados contra el esquema:** 5
- **Fallos de independencia, justificación, referencias o consolidación:** 0
- **Servicios externos utilizados:** 0
