# Inventario inicial

## Estado general

`PENDIENTE_DE_VALIDACION`

## Fuente principal

`arquitectura-editorial-ia-v2.docx`

## Inventario

| Área | Archivos o contenido creado | Finalidad | Estado | Dependencia | Fase futura |
|---|---|---|---|---|---|
| Raíz | `README.md`, `CHANGELOG.md`, `.gitignore`, `LICENSE.md`, `ESTADO_PROYECTO.md` | Gobierno básico del repositorio | Inicial | Decisiones humanas | Paso 3 y siguientes |
| `DOCUMENTACION_FUENTE/` | Documento maestro e inventario | Preservar especificación y trazabilidad | Incorporado | Documento original | Permanente |
| `MANUAL/` | Constitución, siete códigos, glosario y ADR vacío | Autoridad documental | Pendiente | Descomposición del maestro y v1.0 | Paso 4 |
| `MEMORIA/` | Cinco documentos, changelog y evidencias | Memoria persistente | Pendiente | Proyectos e informes futuros | Paso 4+ |
| `AGENTS/` | Plantilla pendiente y fichas de los roles numerados | Definición futura de agentes | Pendiente | Plantilla oficial | Pasos 5 y 6+ |
| `REGLAS/` | Léxico, commits, SLA y umbrales | Reglas transversales | Pendiente | Manual aprobado | Paso 4+ |
| `PROMPTS/` | Directorios por perfil con `.gitkeep` | Prompts versionados | No implementado | Fichas aprobadas y modelos elegidos | Fase futura |
| `WORKFLOWS/` | Cinco flujos y marcador JSON | Procesos y máquina de estados | Pendiente | Decisiones de GR y votación | Fase futura |
| `CHECKLISTS/` | Consejo, personajes y mundos | Validación documental inicial | Pendiente | Fichas de agentes | Paso 6+ |
| `PLANTILLAS/` | Briefs y fichas citadas por la arquitectura | Contratos documentales | Pendiente | Plantilla única | Paso 5+ |
| `LIBROS/` | `activos/` y `archivados/` | Proyectos editoriales | Vacío | Piloto autorizado | Paso 7 |
| `INFORMES/` | Dashboard y métricas | Informes futuros | Pendiente | Datos de ejecución | Paso 6+ |
| `AUDITORIAS/` | Eventos, incidentes, muestreos y consejo | Evidencias auditables | Vacío | Bus y ejecuciones | Automatización futura |
| `TEST/` | Unitarios, integración, casos y sintéticos | Validación | Vacío | Contratos y lógica | Paso 5+ |
| `SCRIPTS/` | `.gitkeep` | Código auxiliar | No implementado | Diseño técnico | Automatización futura |
| `AUTOMATIZACIONES/` | Workflows y triggers vacíos | Orquestación futura | No implementado | Código, APIs y secretos | Automatización futura |
| `RECURSOS/` | Tipografías, paletas, stock y mercado | Recursos editoriales | Vacío | Licencias y proveedores | Producción futura |
| `IMAGENES/`, `PORTADAS/` | `.gitkeep` | Recursos visuales globales | Vacío | Proyectos futuros | Producción futura |
| `.github/` | Workflows vacío y `CODEOWNERS` pendiente | CI y propiedad | No implementado | Reglas y responsables | Fase técnica |
| `src/editorial_ia/` | Núcleo, CLI y agente sintético | Infraestructura local para agentes | Implementado | Python 3.12 y Pydantic 2 | Paso 9 |
| `tests/` | Pruebas unitarias, integración y fixtures | Verificación automatizada del núcleo | Implementado | pytest y pytest-cov | Paso 9 |
| `DOCUMENTACION_TECNICA/` | Guía de infraestructura de agentes | Uso, extensión y límites técnicos | Implementado | ADR-0004 | Paso 9 |
| `AUDITORIAS/eventos/` | JSONL de ejecuciones | Evidencia local append-only | Implementado para desarrollo | Runner local | Paso 9 |

## Numeración verificada

- Roles numerados: `GOB-01`, `GOB-02`, `GOB-03`, `OPS-04` a `OPS-33`, `SUP-34` a `SUP-41`.
- No hay huecos entre 1 y 41.
- La capa editorial contiene 19 roles, aunque el documento maestro declara 18.
- El Consejo `GOB-02` se representa mediante cuatro perfiles: `GOB-02a` a `GOB-02d`.
- Resultado: 41 roles conceptuales y 44 perfiles documentales potencialmente ejecutables.

## Dependencias pendientes

- Arquitectura v1.0 citada pero no incorporada.
- Posición definitiva de GR-1.
- Consolidación de `APROBAR`, `RECHAZAR` y `REQUIERE_CAMBIOS`.
- Convención de nombres.
- Fórmula del ICE.
- Licencia.
