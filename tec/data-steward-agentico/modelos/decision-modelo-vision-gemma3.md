---
tipo: decision
fecha: 2026-11-09
autor: carlos-delgado
resumen: Mantener gemma3:4b como candidato de visión para el prototipo y documentar sus resultados y limitaciones.
---

# Decisión: modelo de visión para extracción de facturas

- **Contexto:** El sistema necesita extraer número de factura, subtotal, impuestos y total de imágenes. Se realizaron pruebas locales con facturas sintéticas de FATURA de distintos formatos.

- **Decisión:** Mantener `gemma3:4b` como candidato provisional de visión mediante Ollama local. Su elección definitiva queda pendiente de una evaluación con el mismo prompt y configuración en todos los documentos.
  - ID local del modelo probado: `68ceab7e468a`.
  - Tamaño observado en disco: `3.4 GB`.
  - Versión de Ollama utilizada: `0.35.0`.
  - Entrada: imagen de factura.
  - Salida: JSON con los cuatro campos solicitados y sus etiquetas como evidencia.

- **Por qué:** El modelo ya se ejecuta localmente y logró extraer correctamente los cuatro campos en algunos documentos. Las mejoras del prompt y del formato de salida permitieron corregir parte de los problemas observados, aunque persisten errores que impiden considerarlo validado para todos los formatos.

- **Alternativas descartadas:** No se realizó una comparación controlada con otros modelos de visión. Bedrock permanece como alternativa pendiente de configurar y evaluar.

## Resultados observados

| Prueba | Resultado |
| --- | --- |
| Factura 2970-559 | Identificó número, subtotal e impuestos; devolvió 826.97 EUR como total cuando la imagen mostraba 828.69 EUR. |
| Otras dos facturas del mismo formato | Se verificaron manualmente los cuatro campos como correctos. |
| Formato con total 634.84 $ | Copió el total como número de factura y subtotal, aunque esos campos no aparecían identificados. |
| Otro documento del formato anterior, total 869.99 $ | Repitió la confusión. Un prompt posterior corrigió el número de factura, pero todavía asignó el total al subtotal. |
| Factura INV18097255 | Extrajo correctamente los cuatro valores; faltaron algunas etiquetas de evidencia. |
| Factura 1Y5M9d-616 | Con el prompt revisado y el esquema JSON, devolvió los cuatro campos esperados, incluido subtotal nulo porque no estaba impreso. |

Las pruebas utilizaron distintas versiones del prompt. Por ello, estos resultados no constituyen una medición única de precisión ni permiten atribuir todos los cambios únicamente al prompt.

## Ajustes realizados

- Solicitar la localización de la etiqueta antes de extraer su valor.
- Devolver `null` cuando un campo no aparezca o no sea legible.
- Solicitar la copia de los importes impresos sin calcular valores faltantes.
- Incluir `valor` y `etiqueta` para cada campo.
- Utilizar un esquema JSON con exactamente los cuatro campos y sin propiedades adicionales.

El esquema restringe la estructura de salida; no garantiza que los valores extraídos sean correctos.

## Condiciones de uso

- Conservar la imagen original y el resultado extraído para su revisión.
- Verificar mediante programación la estructura y los tipos de los datos.
- Tratar los valores ausentes o contradictorios según las reglas del proceso y escalar a revisión humana cuando corresponda.
- Separar la extracción de los cálculos y de la validación de políticas.
- No aceptar o rechazar una factura únicamente con la respuesta del modelo de visión.

## Plan B: Bedrock

Mantener Bedrock como alternativa si la evaluación local no cumple los criterios acordados o si las laptops no están disponibles.

Su activación requiere seleccionar y probar un modelo, configurar el acceso, revisar el presupuesto y definir qué documentos pueden enviarse. No se ha implementado ni validado este respaldo.

## Pendientes

- Guardar la versión exacta del prompt y del esquema JSON utilizados.
- Repetir las pruebas con una configuración fija, incluyendo los formatos donde hubo errores.
- Preparar respuestas esperadas mediante revisión manual.
- Medir aciertos por campo, manejo de campos ausentes y tiempo de respuesta.
- Acordar criterios de aceptación con el equipo antes de cerrar la selección definitiva.

- **Enlaces:**
  - [[tec/data-steward-agentico/modelos/_index|Modelos]]
  - [[tec/data-steward-agentico/modelos/decision-inferencia-en-laptops|Inferencia en laptops]]

## Actualización — 2026-11-11: evaluación controlada (S1-26)

Se evaluó `gemma3:4b` en Ollama local con 20 facturas de 20 plantillas distintas del piloto FATURA. Se utilizó el mismo prompt de cuatro campos y la misma configuración en todo el lote: `temperature=0`, `seed=42`, `num_ctx=4096` y `num_predict=768`.

| Campo | Aciertos / valores anotados | Porcentaje |
| --- | ---: | ---: |
| Folio | 15 / 18 | 83.3 % |
| Subtotal | 10 / 11 | 90.9 % |
| Impuestos | 7 / 7 | 100 % |
| Total | 15 / 15 | 100 % |
| Global | 47 / 51 | 92.2 % |

El tiempo mediano por factura fue de 3.53 segundos. Los 29 campos sin anotación quedaron fuera del cálculo: la falta de anotación no confirma que el dato esté ausente en la imagen. En una revisión visual se comprobó que el modelo confundió un descuento con un impuesto y devolvió un total que no aparecía impreso.

En una prueba aparte con `piloto_001.png`, la salida de 14 campos cumplió el contrato `FacturaExtraida`, pero el RFC del emisor fue incorrecto. Esta prueba no forma parte del 92.2 %.

**Decisión:** usar `gemma3:4b` local para el prototipo, con validación posterior y revisión humana cuando falte evidencia para un dato requerido o haya inconsistencias. Mantener Bedrock como alternativa pendiente de evaluación. La decisión se basa en la viabilidad local observada; no se realizó una comparación de rendimiento con Bedrock.

## Actualización — 2026-11-24: conclusión de S1-26 y límites del extractor integrado

### Decisión de uso

Conservar `gemma3:4b` local como componente experimental del prototipo existente,
con verificación del documento original y decisión final humana. Esta decisión
operativa no acredita precisión suficiente para validar facturas de forma autónoma
ni equivale a aprobar el extractor para producción. La elección definitiva para
el contrato completo queda abierta.

No sustituir el modelo ni cambiar el prompt en vísperas de la demo sin una nueva
evaluación comparable. Bedrock sigue sin una evaluación controlada en este trabajo;
no hay evidencia para afirmar que sea mejor o peor, ni se presenta como respaldo
ya operativo. La conclusión y las limitaciones deben revisarse con el equipo antes
de presentar el alcance del prototipo.

### Por qué los resultados iniciales y los actuales difieren

El registro del 11 de noviembre de esta misma nota sí documenta una evaluación
controlada de 20 facturas de 20 plantillas FATURA. Reportó 47/51 valores anotados
correctos (92.2%): folio 15/18, subtotal 10/11, impuestos 7/7 y total 15/15.
Los 29 campos sin anotación se excluyeron; por tanto, ese porcentaje no mide
la totalidad de las salidas ni el comportamiento ante todos los datos ausentes.
Aquí se conserva como resultado histórico documentado: esta actualización no
repite esa ejecución ni audita nuevamente sus salidas originales.

La evaluación integrada del 23 de noviembre exige 14 campos, conceptos,
transcripción, etiquetas y reglas de negocio sobre otro corpus. No es una repetición
controlada de FATURA: no permite afirmar que el modelo se degradó ni atribuir
la diferencia a una sola causa.

| Aspecto | Evaluación FATURA, 11 nov. | Evaluación integrada, 23 nov. |
| --- | --- | --- |
| Corpus | 20 facturas de 20 plantillas, según el registro anterior | 39 documentos sintéticos: 19 PNG/JPEG y 20 PDF; 4 PDF de dos páginas |
| Campos medidos | 4 | 14 |
| Contexto / generación máxima | 4096 / 768 tokens | 8192 / 4096 tokens |
| Temperatura / semilla | 0 / 42 | 0 / 42 |
| Denominador | Valores con anotación; 29 campos excluidos | Corpus completo para recall, exactitud por campo y clasificación; errores incluidos |
| Resultado destacado | 47/51 anotados correctos (92.2%) | 184/231 emitidos correctos (79.65%); recall 184/505 (36.44%) |
| Clasificación de reglas | No medida | 18/39 correctas (46.15%) |

La extracción actual incluye un filtro que descarta valores sin respaldo en la
transcripción y etiqueta. Las métricas miden la salida posterior al filtro, no
la respuesta bruta del modelo. Los resultados no separan cuánto error proviene
de la lectura visual, la composición de páginas, la generación estructurada o
el filtro. Las reglas pueden rechazar una factura correcta cuando reciben
campos mal leídos; su recomendación no debe confundirse con la validez del original.

### Evidencia reproducible del contrato completo

La ejecución comenzó el 23 de noviembre a las 18:43 de Ciudad de México
(24 de noviembre a las 00:43 UTC), con el código
`eecd6c458e3c356a5e8739ce11c6210236ceb0ff`, Python 3.14.5 y `gemma3:4b`.
Digest del modelo:
`68ceab7e468a31c988b44d5a4984a0e21f58c4f7158c6ce29c1804babac38df7`.
El manifiesto identifica el código, las bibliotecas y los documentos mediante hashes.

Se mantuvieron el mismo prompt, esquema y configuración durante los 39 intentos:
`temperature=0`, `seed=42`, `num_ctx=8192`, `num_predict=4096` y espera HTTP de
180 segundos. Se comenzó con un documento y se continuó con `--reanudar`,
sin reemplazar salidas ni reintentar selectivamente los errores. La fecha de
recepción de las referencias fue 2026-11-02. La verdad de referencia solo se usa
para calificar, nunca como respuesta del extractor.

Los PDF se rasterizaron completos a 150 dpi mediante el adaptador PyMuPDF 1.28.2
de esa ejecución. El soporte posterior con PDFium del PR #39 es otra implementación:
esta medición no demuestra su precisión ni debe atribuirse a ese cambio.
La base fue `dsa_pruebas`, con escrituras revertidas por caso y embeddings de prueba
`falso`; no se midió la calidad semántica del RAG.

| Indicador | Resultado |
| --- | --- |
| Intentos / pendientes | 39 / 0 |
| Llegaron a pausa humana | 30/39 (76.92%) |
| Fallos de extracción | 9/39 (23.08%) |
| Precisión de valores emitidos no vacíos | 184/231 (79.65%) |
| Recall sobre los valores esperados del corpus | 184/505 (36.44%) |
| Exactitud de clasificación | 18/39 (46.15%) |
| Macro F1 | 40.19% |
| Recomendaciones de aceptación | 0, incluidas las 11 facturas esperadas como aceptadas |

### Exactitud normalizada por campo

El denominador es 39 e incluye errores. Las coincidencias incluyen ausencias
correctas; por ello, por ejemplo, el resultado de retenciones no significa que
se hayan leído 29 importes presentes. La precisión de valores emitidos de arriba
excluye los null correctos.

| Campo | Coincidencias / corpus | Exactitud |
| --- | --- | --- |
| folio | 10/39 | 25.64% |
| fecha | 17/39 | 43.59% |
| emisor_nombre | 22/39 | 56.41% |
| emisor_rfc | 8/39 | 20.51% |
| emisor_direccion | 12/39 | 30.77% |
| receptor_nombre | 12/39 | 30.77% |
| receptor_rfc | 8/39 | 20.51% |
| moneda | 17/39 | 43.59% |
| subtotal | 19/39 | 48.72% |
| impuestos | 16/39 | 41.03% |
| tasa_iva | 13/39 | 33.33% |
| retenciones | 29/39 | 74.36% |
| total | 19/39 | 48.72% |
| condiciones_pago | 13/39 | 33.33% |

### Hallazgos y límites de la decisión

- Ocho fallos registran «Ollama no completó la extracción» y uno quedó sin campos
  utilizables tras el filtro. El registro no distingue `done_reason=length` de
  ausencia de `done`; agotar tokens es una hipótesis, no un diagnóstico confirmado.
- R-001 aparece en 29 de los 30 casos con pausa. Ocho de los 18 aciertos de categoría
  omiten al menos una regla esperada: acertar la categoría no prueba una explicación correcta.
- La confianza se conserva en null: no hay medida calibrada. No debe presentarse
  una autoevaluación del modelo como probabilidad de acierto verificada.
- Conceptos, bbox y confianza no se califican como exactitud de extracción. Los
  conceptos sí pueden afectar las reglas. Algunos escenarios de referencia dependen
  de confianza simulada o texto oculto que la extracción visual no reproduce.
- Piloto_001 se usó durante el ajuste previo del extractor: es un corpus de desarrollo,
  no una prueba independiente de generalización.
- El 79.65% no implica que el 79.65% de las facturas estén bien extraídas. Los errores
  y las omisiones son materiales; el extractor completo no queda validado.

### Alcance de cierre de S1-26

Quedan documentadas una evaluación controlada de al menos 20 facturas, la precisión
por campo y la decisión de uso local limitado. Cerrar esta tarea documental no
certifica el desempeño del extractor ni cierra S3-11 (validación en dev) o S3-13
(revisión de la evaluación del flujo). No se acordó ni se demuestra aquí un umbral
de aceptación de producción.

Para una selección definitiva, comparar alternativas con el mismo contrato,
preprocesamiento, corpus y configuración fija por ejecución; registrar respuesta
bruta y posterior al filtro y separar un conjunto de evaluación no usado para ajustar
el prompt. Cualquier nueva medición debe conservar esta línea base.

### Fuentes

- [Conclusiones y alcance de la ejecución](https://github.com/CEMxBanamex/Banamex_Monorepo/blob/f1e004fecc0c45719e4603461fe766e786083128/docs/evidencias/s3-13/ejecucion-2026-11-23/README.md).
- [Manifiesto reproducible](https://github.com/CEMxBanamex/Banamex_Monorepo/blob/f1e004fecc0c45719e4603461fe766e786083128/docs/evidencias/s3-13/ejecucion-2026-11-23/ejecucion.json).
- [Resumen y detalle por campo](https://github.com/CEMxBanamex/Banamex_Monorepo/blob/f1e004fecc0c45719e4603461fe766e786083128/docs/evidencias/s3-13/ejecucion-2026-11-23/resumen.json).
- [Clasificación por documento](https://github.com/CEMxBanamex/Banamex_Monorepo/blob/f1e004fecc0c45719e4603461fe766e786083128/docs/evidencias/s3-13/ejecucion-2026-11-23/casos.csv).
- [PR #36: evaluación del flujo](https://github.com/CEMxBanamex/Banamex_Monorepo/pull/36).
- [PR #39: soporte PDF posterior](https://github.com/CEMxBanamex/Banamex_Monorepo/pull/39).
- [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|Propuesta de Iris sobre confianza y contrato de 14 campos]].
- [[tec/data-steward-agentico/tareas/carlos-delgado|Tareas de Carlos Delgado]].
