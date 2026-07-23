# Instrucciones generales para Codex

## Propósito

Este repositorio define y, por fases autorizadas, implementa Editorial IA: un sistema editorial trazable que transforma una idea en productos editoriales sin sustituir las decisiones humanas obligatorias.

## Autoridad documental

Ante conflicto, aplica este orden de mayor a menor autoridad:

1. `MANUAL/CONSTITUCION.md`.
2. `MANUAL/CODIGOS/`.
3. `MEMORIA/`, siempre que tenga evidencia y aprobación exigible.
4. `REGLAS/`.
5. Fichas de `AGENTS/`.
6. `WORKFLOWS/`.
7. Instrucción concreta de la tarea.

Las instrucciones `AGENTS.md` locales especializan este archivo, pero no pueden contradecirlo. Si dos fuentes de igual rango discrepan o falta una decisión humana imprescindible, detente, registra el bloqueo y solicita resolución.

## Reglas obligatorias

- No inventes decisiones editoriales, comerciales, legales, de seguridad ni preferencias del autor.
- Toda decisión debe citar el archivo o la sección que la sustenta. Si la fuente aún no existe, marca la dependencia como `PENDIENTE`.
- No omitas GR-1 a GR-4 ni sustituyas la aprobación humana.
- No sobrescribas silenciosamente archivos versionados. Conserva el historial Git y usa versiones o checkpoints para artefactos editoriales.
- No implementes más de una fase ni amplíes el alcance sin autorización expresa.
- Mantén separados documentación, prompts, código, proyectos editoriales y resultados generados.
- No expongas ni confirmes secretos, tokens, contraseñas o credenciales. Usa variables de entorno y archivos ignorados por Git.
- Actualiza `CHANGELOG.md` y `ESTADO_PROYECTO.md` en cada cambio material.
- Actualiza `MANUAL/REGISTRO_DECISIONES/` cuando una decisión cambie arquitectura, autoridad, contratos o comportamiento.
- No conviertas contenido `PENDIENTE`, simulado o diseñado en una afirmación de implementación real.

## Convenciones

- Conserva los nombres estructurales existentes y no hagas renombrados masivos sin ADR.
- Identificadores de agentes: `GOB-XX`, `OPS-XX` y `SUP-XX`; miembros del Consejo: `GOB-02a` a `GOB-02d`.
- Proyectos: `PID-AAAAMMDD-XXXX`.
- Documentos generales nuevos: `kebab-case.md`, salvo nombres canónicos ya definidos por la arquitectura.
- Artefactos de libro: prefijos `ms_`, `cov_`, `ill_`, `inf_`, `aud_`, `web_`, `mkt_`, `rpt_`, `per_`, `mnd_`, `sys_`, `met_` y `ejer_`.
- Commits: `[TIPO][ALCANCE] descripción breve`; usa un PID como alcance cuando el cambio pertenezca a un libro.

## Comprobaciones actuales

Ejecuta desde la raíz, según corresponda:

```powershell
git status --short --branch
git diff --check
Get-Content WORKFLOWS/maquinas_estado/proyecto.json -Raw | ConvertFrom-Json | Out-Null
Get-ChildItem AGENTS -Recurse -File -Filter '*.md'
```

Antes de finalizar, comprueba además archivos esperados, enlaces relativos afectados, numeración de agentes, ausencia de secretos y que el estado documentado coincida con lo realmente implementado.

## Informe final

Indica de forma concisa:

- resultado y alcance;
- archivos principales modificados;
- comprobaciones ejecutadas;
- commit, si se solicitó;
- elementos pendientes, simulados o bloqueados;
- confirmación de que no se avanzó a otra fase.

