# Validación documental de secciones de agente

- **Versión:** 1.0
- **Fecha:** 2026-07-23
- **Estado:** `DEFINIDO`
- **Fuente:** `../../../AGENTS/_TEMPLATE/AGENT_TEMPLATE.md` y `../../../MANUAL/REGISTRO_DECISIONES/ADR-0002-plantilla-unica-agentes.md`
- **Responsable de aprobación:** Responsable de Calidad

## Objetivo

Comprobar que una ficha contiene todos los apartados obligatorios antes de declararla completa.

## Lista canónica

1. Identificador.
2. Nombre.
3. Capa.
4. Versión.
5. Estado.
6. Misión.
7. Objetivo.
8. Alcance.
9. Responsabilidades.
10. Acciones prohibidas.
11. Documentos que debe consultar.
12. Entradas obligatorias.
13. Validación de entradas.
14. Proceso paso a paso.
15. Herramientas permitidas.
16. Herramientas prohibidas.
17. Formato exacto de salida.
18. Artefactos generados.
19. Criterios de aceptación.
20. Lista de comprobación.
21. Indicadores de calidad.
22. Errores habituales.
23. Clasificación de errores aplicable.
24. Número máximo de reintentos.
25. Condiciones para devolver trabajo.
26. Agente anterior.
27. Agente siguiente.
28. Condiciones para escalar al humano.
29. Registro de auditoría.
30. Casos de prueba.
31. Ejemplo de entrada.
32. Ejemplo de salida.
33. Historial de versiones.

## Procedimiento

1. Leer los encabezados `##` de la ficha.
2. Normalizar únicamente el prefijo numérico.
3. Compararlos con la lista canónica.
4. Comprobar que cada sección contiene contenido o una justificación de `NO_APLICA`.
5. Rechazar encabezados duplicados.
6. Comprobar enlaces a contratos comunes.

## Criterio

- `SUPERADA`: 33 secciones presentes una vez y con contenido.
- `FALLIDA`: falta, se duplica o está vacía alguna sección.

## Resultado sobre la plantilla oficial

`SUPERADA`

- Secciones esperadas: 33.
- Secciones encontradas: 33.
- Ausentes: 0.
- Duplicadas: 0.
- Inesperadas: 0.
- Vacías: 0.
- Fecha de ejecución: 2026-07-23.
