# EDITORIAL_IA

## Finalidad

Repositorio documental y técnico para la arquitectura v2.0 de Editorial IA.

## Estado

`INFRAESTRUCTURA_BASE_IMPLEMENTADA`

La estructura documental y las seis fichas de Gobierno están definidas. Existe
una infraestructura Python local y solo el agente sintético `TEST-AGENT-001` es
ejecutable. Los agentes de producción, workflows operativos, servicios externos y
automatizaciones todavía no están implementados.

## Fuente

`DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`

## Responsable futuro

Consejo Editorial y responsable humano del proyecto.

## Índice documental

### Autoridad

- [Constitución](MANUAL/CONSTITUCION.md)
- [Código de estilo](MANUAL/CODIGOS/CODIGO_ESTILO.md)
- [Código de calidad](MANUAL/CODIGOS/CODIGO_CALIDAD.md)
- [Código de producción](MANUAL/CODIGOS/CODIGO_PRODUCCION.md)
- [Código de seguridad](MANUAL/CODIGOS/CODIGO_SEGURIDAD.md)
- [Código de aprendizaje](MANUAL/CODIGOS/CODIGO_APRENDIZAJE.md)
- [Código comercial](MANUAL/CODIGOS/CODIGO_COMERCIAL.md)
- [Glosario](MANUAL/GLOSARIO.md)
- [Arquitectura del sistema](MANUAL/ARQUITECTURA_SISTEMA.md)
- [Jerarquía de instrucciones](MANUAL/REGISTRO_DECISIONES/ADR-0001-jerarquia-instrucciones.md)

### Memoria Editorial

- [Decisiones editoriales](MEMORIA/decisiones_editoriales.md)
- [Errores históricos](MEMORIA/errores_historicos.md)
- [Mejores prácticas](MEMORIA/mejores_practicas.md)
- [Estilo del autor](MEMORIA/estilo_autor.md)
- [Conocimientos acumulados](MEMORIA/conocimientos_acumulados.md)

### Seguimiento

- [Informe de descomposición](INFORMES/informe-descomposicion-arquitectura-v2.md)
- [Auditoría de la fase inicial](INFORMES/AUDITORIA_FASE_INICIAL.md)
- [Estado del proyecto](ESTADO_PROYECTO.md)
- [Registro de cambios](CHANGELOG.md)
- [Documento maestro](DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx)

### Contratos de agentes

- [Plantilla única](AGENTS/_TEMPLATE/AGENT_TEMPLATE.md)
- [Contrato de entrada](PLANTILLAS/contrato-entrada-agente.md)
- [Contrato de salida](PLANTILLAS/contrato-salida-agente.md)
- [Informe de rechazo](PLANTILLAS/informe-rechazo.md)
- [Informe de error](PLANTILLAS/informe-error.md)
- [Registro de decisión](PLANTILLAS/registro-decision.md)
- [Checklist común](PLANTILLAS/checklist-agente.md)
- [ADR-0002](MANUAL/REGISTRO_DECISIONES/ADR-0002-plantilla-unica-agentes.md)

### Gobierno documental

- [Orquestador](AGENTS/GOB/GOB-01_ORQUESTADOR.md)
- [Consejo Editorial](AGENTS/GOB/GOB-02_CONSEJO/)
- [Auditor](AGENTS/GOB/GOB-03_AUDITOR.md)
- [Esquema de votación](PLANTILLAS/votacion-consejo.schema.json)
- [Checklist de votación](CHECKLISTS/GOB-02_votacion.md)
- [ADR-0003](MANUAL/REGISTRO_DECISIONES/ADR-0003-votacion-consejo-editorial.md)
- [Informe del paso 6](INFORMES/informe-agentes-gobierno.md)

### Proyecto piloto

- [PID-PILOTO-001](LIBROS/activos/PID-PILOTO-001/README.md)
- [Estado inicial](LIBROS/activos/PID-PILOTO-001/_meta/estado.json)
- [Pruebas de integración](TEST/integracion/proyecto-piloto/casos.md)
- [Informe del piloto](INFORMES/informe-prueba-piloto-001.md)

### Infraestructura técnica de agentes

- [Guía técnica](DOCUMENTACION_TECNICA/infraestructura-agentes.md)
- [ADR-0004](MANUAL/REGISTRO_DECISIONES/ADR-0004-infraestructura-base-agentes.md)
- [Informe del paso 9](INFORMES/informe-paso-09-infraestructura-agentes.md)
- [Código fuente](src/editorial_ia/)
- [Pruebas automatizadas](tests/)
- [Eventos de auditoría](AUDITORIAS/eventos/)

## Inicio rápido

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\editorial-ia.exe run --agent TEST-AGENT-001 --project PID-PILOTO-001 --input "Prueba de infraestructura"
```
