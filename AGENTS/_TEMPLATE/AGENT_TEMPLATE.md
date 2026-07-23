# {IDENTIFICADOR} — {NOMBRE}

- **Versión:** `{SEMVER}`
- **Fecha:** `{AAAA-MM-DD}`
- **Estado:** `BORRADOR | PENDIENTE_DE_VALIDACION | DEFINIDO | NO_IMPLEMENTADO`
- **Capa:** `{GOBIERNO | OPERATIVA_CREATIVA | OPERATIVA_EDITORIAL | OPERATIVA_COMERCIAL | SOPORTE}`
- **Fuente:** `{RUTA_Y_SECCION}`
- **Responsable de aprobación:** `{ROL_HUMANO_U_ORGANO}`

> Esta plantilla define un contrato documental. Completarla no implementa ni activa un agente.

## 1. Identificador

`{GOB-XX | OPS-XX | SUP-XX}`

Debe ser único y respetar la numeración aprobada.

## 2. Nombre

`{NOMBRE_CANONICO}`

## 3. Capa

`{CAPA_CANONICA}`

## 4. Versión

`{SEMVER}`

## 5. Estado

`{ESTADO_DOCUMENTAL}`

Indicar separadamente si existe o no una implementación técnica.

## 6. Misión

{Razón permanente de existencia del agente, en una frase.}

## 7. Objetivo

{Resultado concreto que debe lograr en una ejecución.}

## 8. Alcance

### Incluye

- {RESPONSABILIDAD_DENTRO_DE_ALCANCE}

### Excluye

- {RESPONSABILIDAD_FUERA_DE_ALCANCE}

## 9. Responsabilidades

1. {RESPONSABILIDAD_1}
2. {RESPONSABILIDAD_2}

## 10. Acciones prohibidas

- {ACCION_PROHIBIDA}
- Tomar decisiones humanas o editoriales fuera de su autoridad.
- Omitir trazabilidad, puertas humanas o controles aplicables.

## 11. Documentos que debe consultar

En orden de autoridad:

1. `{DOCUMENTO_OBLIGATORIO}`
2. `{DOCUMENTO_CONDICIONAL}`

Cada consulta debe registrar versión o referencia.

## 12. Entradas obligatorias

| Campo | Tipo o formato | Obligatorio | Fuente |
|---|---|---|---|
| `{CAMPO}` | `{TIPO}` | Sí | `{ORIGEN}` |

Usar el [contrato de entrada](../../PLANTILLAS/contrato-entrada-agente.md).

## 13. Validación de entradas

1. Comprobar presencia y formato.
2. Comprobar PID, estado y versión.
3. Comprobar permisos y puerta humana aplicable.
4. Rechazar mediante [informe de rechazo](../../PLANTILLAS/informe-rechazo.md) si la entrada no es válida.

## 14. Proceso paso a paso

1. {PASO_DE_PREPARACION}
2. {PASO_DE_EJECUCION}
3. {PASO_DE_AUTOCONTROL}
4. {PASO_DE_ENTREGA_Y_REGISTRO}

## 15. Herramientas permitidas

| Herramienta | Finalidad | Restricciones |
|---|---|---|
| `{HERRAMIENTA}` | `{FINALIDAD}` | `{LIMITES}` |

## 16. Herramientas prohibidas

- `{HERRAMIENTA_O_CAPACIDAD}`
- Cualquier herramienta no autorizada expresamente.

## 17. Formato exacto de salida

```text
{ESQUEMA_O_ESTRUCTURA_EXACTA}
```

Usar el [contrato de salida](../../PLANTILLAS/contrato-salida-agente.md).

## 18. Artefactos generados

| Artefacto | Ruta esperada | Versionado |
|---|---|---|
| `{NOMBRE}` | `{RUTA}` | `{REGLA_DE_VERSION}` |

## 19. Criterios de aceptación

- [ ] {CRITERIO_BINARIO_Y_VERIFICABLE}
- [ ] Salida trazable a las entradas y normas consultadas.

## 20. Lista de comprobación

Usar [checklist común de agente](../../PLANTILLAS/checklist-agente.md) y añadir comprobaciones específicas:

- [ ] {COMPROBACION_ESPECIFICA}

## 21. Indicadores de calidad

| Indicador | Fórmula o evidencia | Umbral |
|---|---|---|
| `{INDICADOR}` | `{MEDICION}` | `{UMBRAL}` |

## 22. Errores habituales

| Error | Señal de detección | Prevención |
|---|---|---|
| `{ERROR}` | `{SEÑAL}` | `{PREVENCION}` |

## 23. Clasificación de errores aplicable

- `{E1-E7_O_CATEGORIA_APROBADA}`

No definir nuevas categorías sin ADR o actualización del Código correspondiente.

## 24. Número máximo de reintentos

`{NUMERO}`

La arquitectura propone un máximo general de tres; cualquier excepción requiere fuente y aprobación.

## 25. Condiciones para devolver trabajo

- {CONDICION_OBJETIVA_DE_DEVOLUCION}
- Entrada incompleta, contradictoria o no autorizada.

## 26. Agente anterior

`{IDENTIFICADOR | NINGUNO}`

Indicar artefacto y condición de entrega.

## 27. Agente siguiente

`{IDENTIFICADOR | NINGUNO}`

Indicar artefacto y condición de aceptación.

## 28. Condiciones para escalar al humano

- Falta una decisión humana imprescindible.
- Existe conflicto entre fuentes de igual autoridad.
- Se alcanza el máximo de reintentos.
- {CONDICION_ESPECIFICA}

## 29. Registro de auditoría

Registrar como mínimo:

- PID y ejecución;
- agente y versión;
- entradas y salidas por referencia;
- normas consultadas;
- decisiones y justificaciones;
- tiempos, reintentos y resultado;
- escalado o aprobación humana.

## 30. Casos de prueba

| ID | Escenario | Entrada | Resultado esperado |
|---|---|---|---|
| `{CP-ID}` | `{ESCENARIO}` | `{FIXTURE}` | `{RESULTADO}` |

Incluir casos válido, inválido, rechazo, reintento y escalado.

## 31. Ejemplo de entrada

```yaml
estado: EJEMPLO_NO_EJECUTABLE
datos:
  pendiente: true
```

El ejemplo debe cumplir el contrato de entrada y no contener información real sensible.

## 32. Ejemplo de salida

```yaml
estado: EJEMPLO_NO_EJECUTABLE
resultado:
  pendiente: true
```

El ejemplo debe cumplir el contrato de salida y no afirmar una ejecución real.

## 33. Historial de versiones

| Versión | Fecha | Cambio | Aprobación |
|---|---|---|---|
| `{SEMVER}` | `{AAAA-MM-DD}` | `{CAMBIO}` | `{RESPONSABLE}` |
