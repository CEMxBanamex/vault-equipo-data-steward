---
tipo: decision
fecha: 2026-11-09
autor: carlos-delgado
resumen: Seleccionar embeddinggemma:300m para los embeddings del prototipo tras una prueba inicial de recuperación.
---

# Decisión: modelo de embeddings del prototipo

- **Contexto:** El sistema necesita recuperar información relacionada con las consultas del usuario. Para ello, los documentos y las consultas deben convertirse en vectores utilizando el mismo modelo de embeddings.

- **Decisión:** Utilizar `embeddinggemma:300m` mediante Ollama local para generar los embeddings de los documentos y las consultas.
  - ID local del modelo probado: `85462619ee72`.
  - Dimensiones del vector obtenido: `768`.
  - Tamaño de descarga observado: `621 MB`.
  - Versión de Ollama utilizada: `0.35.0`.

- **Por qué:** El modelo pudo ejecutarse localmente y recuperar el documento esperado en tres consultas de una prueba inicial con información sintética. Esto permite avanzar con el prototipo utilizando el modelo ya instalado.

- **Alternativas descartadas:** No se compararon otros modelos de embeddings en esta prueba. Se selecciona el modelo instalado para iniciar el prototipo; su desempeño deberá evaluarse con más documentos y consultas.

## Evidencia de la prueba

Se utilizaron tres documentos sintéticos sobre proveedor no identificado, diferencias entre importes e imágenes ilegibles. No representan políticas confirmadas de Banamex.

| Consulta | Documento esperado | Documento recuperado | Similitud coseno |
| --- | --- | --- | --- |
| No se puede identificar quien emitio la factura. | DEMO-01: proveedor no identificado | DEMO-01 | 0.5630 |
| El importe final no cuadra con los demas montos. | DEMO-02: consistencia de importes | DEMO-02 | 0.5141 |
| La foto esta desenfocada y no distingo las letras. | DEMO-03: documento ilegible | DEMO-03 | 0.3857 |

**Resultado:** 3 de 3 consultas recuperaron el documento esperado en primera posición.

La similitud coseno indica cercanía entre vectores; no es una probabilidad de que la respuesta sea correcta. Esta prueba verifica el funcionamiento inicial y no demuestra precisión general.

## Condiciones de uso

- Utilizar el mismo modelo para indexar documentos y generar los vectores de las consultas.
- Registrar la etiqueta y el ID del modelo utilizado.
- Si cambia el modelo, regenerar los embeddings del catálogo.
- Mantener separadas la recuperación de información y la validación de reglas de negocio.

## Pendientes

- Probar más documentos, paráfrasis y consultas sin información relevante.
- Evaluar la recuperación con fuentes autorizadas del proyecto.
- Integrar los vectores en la base de datos del sistema.
- Definir criterios de aceptación antes de utilizarlo en el flujo completo.

- **Enlaces:**
  - [[tec/data-steward-agentico/modelos/_index|Modelos]]
  - [[tec/data-steward-agentico/modelos/mismo-modelo-de-embeddings|Mismo modelo para documentos y consultas]]
  -