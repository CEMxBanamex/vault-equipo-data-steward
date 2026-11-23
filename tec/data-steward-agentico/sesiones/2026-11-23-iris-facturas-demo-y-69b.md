---
tipo: sesion
fecha: 2026-11-23
autor: iris
resumen: Facturas de la demo (S3-23) con sus respaldos y regla R-019 de la lista 69-B del SAT (S3-26); avisos para el ensayo y la demo.
---
# Sesión 2026-11-23: facturas de la demo y regla 69-B

Trabajo con Mario. Código en el repo de código (rama `datos/demo-y-69b`, PR a `dev`).

## Facturas de la demo (S3-23)
Probadas con `validar_reglas` sobre la extracción de referencia y la base sembrada, con fecha de recepción del 25 nov. Registro y prueba: `datos/evaluacion/facturas_demo.yaml` y `datos/tests/test_facturas_demo.py`. Archivos en `db/semillas/sinteticos/facturas/evaluacion/`.

| Escenario | Factura | Respaldo | Resultado | Qué mostrar |
|---|---|---|---|---|
| Correcta | `piloto_001.png` | `piloto_003.png` | Aceptada | Sin hallazgos; el analista confirma |
| Total que no cuadra | `piloto_012.png` | `piloto_014.jpg` | Rechazada · R-014 | 159,900.55 + 25,584.09 = 185,484.64, pero el total impreso es 185,884.64 |
| Campo faltante | `piloto_021.jpg` | `piloto_020.png` | Rechazada · R-001 | No trae el RFC del emisor (el respaldo no trae folio) |
| Baja confianza | `piloto_035.jpg` | `piloto_036.pdf` | Revisión humana · R-003 | Escaneo borroso: se manda a revisión en vez de rechazar |

## Avisos para el ensayo y la demo
- **No usar `factura_1041.png`** (F-1041 del mockup): ya está en la base y sale rechazada por duplicado (R-015).
- **Cada archivo solo puede subirse una vez por base.** Si en el ensayo del martes se suben estas 4, el miércoles R-015 las marca como duplicadas. Opciones: usar los respaldos en el ensayo, o volver a sembrar `dsa_dev` antes de la demo.
- **La de baja confianza depende de [[tec/data-steward-agentico/tareas/carlos-delgado|Carlos Delgado]] (S3-11):** si `extraer_campos_factura` no devuelve confianza por campo, R-003 solo avisa y la factura no va a revisión. Ver [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|la propuesta de confianza]].
- **Formatos:** dos son PNG, una JPG y el respaldo de baja confianza es PDF; confirmar con Carlos Delgado que la extracción acepta los tres.

## Regla 69-B (S3-26)
- **R-019 v1.0** con la política nueva **P-005** (`tipo: facturas`, cita el art. 69-B del CFF). Si el RFC del emisor está en la lista como *definitivo*, Rechazado; como *presunto*, revisión humana; *desvirtuado* o *sentencia favorable*, sin hallazgo.
- Lista de prueba con RFC sintéticos: `datos/reglas/lista_69b.csv` (`EFO150101AB1` definitivo, `PRE160202CD2` presunto, `DES170303EF3` desvirtuado). En producción se reemplaza con la descarga del SAT con `RUTA_LISTA_69B`.
- Pregunta nueva en `preguntas_rag.yaml` para que el RAG encuentre P-005. Al cargar la semilla, P-005 entra al RAG y R-019 a la tabla de reglas.

## Pruebas
272 en verde contra PostgreSQL + pgvector.

## Actualización 23 nov., tarde: facturas que ve dev-ana
- En dev la app y el chat entran como `dev-ana` (analista), que solo ve Grupo Financiero Demo, Banca Demo y Comercializadora Demo. `piloto_001.png` es de Servicios Corporativos Demo y además ya se usó en la prueba de S3-11, así que la factura correcta pasa a ser **`piloto_003.png`** con respaldo **`piloto_005.png`**.
- Las otras tres principales sí son de entidades de `dev-ana`. El respaldo de baja confianza (`piloto_036.pdf`) no; solo sirve con el administrador.
- Cambio en el repo de código: rama `datos/iris-demo-dev-ana`. La prueba revisa que el receptor de cada factura principal sea una entidad de `dev-ana`.
- El guion quedó en [[tec/data-steward-agentico/plan-de-trabajo/propuesta-guion-demo-25-nov-iris|guion de la demo]] (S3-24).
