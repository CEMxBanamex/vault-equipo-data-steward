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