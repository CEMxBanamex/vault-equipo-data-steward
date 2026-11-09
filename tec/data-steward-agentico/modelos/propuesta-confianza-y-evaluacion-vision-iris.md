---
tipo: propuesta
fecha: 2026-11-09
autor: iris
resumen: Pedir confianza por campo al modelo de visión y medirlo con las facturas sintéticas que ya tienen respuesta esperada.
---
# Propuesta: confianza por campo y evaluación del modelo de visión

- **Nota que se cambiaría:** [[tec/data-steward-agentico/tools/extraer-campos-factura|extraer_campos_factura]] y la decisión de modelo de visión de Carlos Delgado (en su rama).
- **Qué propongo:**
  - Que `extraer_campos_factura` devuelva, además de `valor` y `etiqueta`, una `confianza` de 0 a 100 por campo (por ejemplo, con logprobs o con una autoevaluación del modelo). La regla R-003 marca para revisión humana todo campo con menos de 80 %; sin confianza no puede evaluarse.
  - Usar nuestras facturas sintéticas para los pendientes de la prueba de visión ("preparar respuestas esperadas" y "medir aciertos por campo"): 39 facturas de evaluación en 4 diseños y 4 formatos, cada una con su verdad de referencia, y `scripts/evaluar.py`, que da la precisión por campo con normalización de montos, fechas y RFC. Están en el repo de código, `datos/sinteticos/facturas/evaluacion/`.
  - Para FATURA, `scripts/fatura_piloto.py` convierte sus anotaciones al mismo formato. Ojo: sus facturas no son CFDI (no traen RFC del receptor y vienen en EUR o $), así que sirven para medir la extracción, no las reglas.
  - Llaves de los campos: `folio, fecha, emisor_nombre, emisor_rfc, emisor_direccion, receptor_nombre, receptor_rfc, moneda, subtotal, impuestos, tasa_iva, retenciones, total, condiciones_pago`, y los `conceptos` como lista.
- **Por qué:** la confianza es lo que permite sugerir revisión humana cuando el modelo duda, en lugar de rechazar por un dato mal leído. Y medir con las mismas facturas permite comparar prompts y modelos con una sola configuración.
- **Estado:** pendiente
