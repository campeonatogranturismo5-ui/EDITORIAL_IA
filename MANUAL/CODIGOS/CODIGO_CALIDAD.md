# Código de calidad

- **Versión:** 2.0
- **Fecha:** 2026-07-23
- **Estado:** `PENDIENTE_DE_VALIDACION`
- **Fuente:** `../../DOCUMENTACION_FUENTE/arquitectura-editorial-ia-v2.docx`, secciones 4, 5 y 16
- **Responsable de aprobación:** Responsable de Calidad, Auditor y responsable humano

## Niveles

| Nivel | Uso | ICE mínimo |
|---|---|---:|
| A — Obra | Libros del sello | 85 |
| B — Profesional | Lead magnets y artículos largos | 75 |
| C — Operativo | Borradores internos y documentación | 60 |

La fórmula, dimensiones y ponderación del ICE no están definidas en la fuente y requieren validación humana.

## Umbrales por entregable

- Manuscrito: máximo 0,5 errores por 1.000 palabras; coherencia temática mínima 0,9; originalidad mínima 0,85.
- PDF: tipografía embebida, marcadores funcionales y validación PDF/A-3.
- EPUB: EPUBCheck sin errores y WCAG 2.1 AA.
- Portada: 300 DPI como mínimo, legible a 80 px y conforme con Amazon KDP.
- Audiolibro: -23 LUFS ± 2, sin artefactos y nombres propios validados.
- Infografías: 300 DPI, legibles a 400 px y con texto alternativo.
- Ejercicios: solución, tiempo y dificultad etiquetada.
- Personajes: ficha completa y aprobada.
- Mundos: reglas físicas, mágicas y sociales consistentes.

## Líneas de defensa

1. Autocontrol del agente productor.
2. Validación del agente receptor.
3. Auditoría independiente sobre una muestra aleatoria del 20 %.
4. Revisión colegiada de entregables críticos por el Consejo.

## Métricas continuas

- Rechazo por agente.
- Tiempo medio por estado.
- Escalado humano.
- ICE por libro.
- Coste por libro.
- Disidencia del Consejo; si supera el 30 %, revisar prompts.
- Métricas comerciales del [Código comercial](CODIGO_COMERCIAL.md).

## Revisiones

- Automática.
- Entre agentes.
- Humana mediante GR-1 a GR-4.
- Colegiada mediante el Consejo.

## Criterios pendientes

- Fórmula y validación estadística del ICE.
- Herramienta y corpus para originalidad.
- Método para medir coherencia temática.
- Compatibilidad del requisito PDF/A-3 con cada canal de impresión.
- Muestreo aleatorio reproducible.

