# Checklist de votación del Consejo

- **Versión:** `1.0.0`
- **Fecha:** `2026-07-23`
- **Estado:** `DEFINIDO` documentalmente
- **Fuente:** `../MANUAL/CODIGOS/CODIGO_PRODUCCION.md` y `../MANUAL/REGISTRO_DECISIONES/ADR-0003-votacion-consejo-editorial.md`
- **Responsable de aprobación:** Consejo Editorial y responsable humano

## Antes de votar

- [ ] Existe una convocatoria única y un `audit_ref`.
- [ ] Los cuatro miembros reciben el mismo `dossier_ref` y `dossier_hash`.
- [ ] El expediente identifica PID, puerta y criterios.
- [ ] Cada miembro está aislado de los votos ajenos.

## Cada voto

- [ ] Pertenece a uno de `GOB-02a`, `GOB-02b`, `GOB-02c` o `GOB-02d`.
- [ ] Usa `APROBAR`, `RECHAZAR` o `REQUIERE_CAMBIOS`.
- [ ] Incluye una justificación no vacía.
- [ ] Incluye al menos una referencia normativa.
- [ ] Declara `sealed: true` y `saw_other_votes: false`.

## Consolidación

- [ ] Están presentes exactamente los cuatro votos.
- [ ] `approve_count + non_approve_count = 4`.
- [ ] La regla coincide con `4-0`, `3-1`, `2-2`, `1-3` o `0-4`.
- [ ] 4-0 produce `APROBAR`, sin disidencia.
- [ ] 3-1 produce `APROBAR`, con disidencia.
- [ ] 2-2 produce `REQUIERE_CAMBIOS`, con disidencia y escalado humano.
- [ ] 1-3 y 0-4 producen `RECHAZAR`, con incidente E5 documental.
- [ ] Si la puerta es GR-1 a GR-4, la aprobación humana permanece obligatoria.

## Cierre

- [ ] La consolidación no altera los votos sellados.
- [ ] La decisión humana se registra por referencia; no se inventa.
- [ ] La ejecución está marcada como simulada.
- [ ] No se usaron modelos de IA ni bus de eventos.
