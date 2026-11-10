---
tipo: sesion
fecha: 2026-11-09
autor: iris
resumen: Frente de datos con Mario (4 al 9 nov.); de mi parte quedaron validar_reglas, consultar_calidad, las reglas de calidad, el catálogo de reglas y los casos de referencia del piloto.
---
# Sesión 2026-11-09: frente de datos (parte de Iris)

Trabajo en pareja con Mario. Su sesión del mismo día cubre las vistas, la capa semántica, el glosario y el catálogo de datos. El código está en el repo de código, carpeta `datos/` (rama `datos/fases-0-a-4`), con su `README.md`.

## Qué se hizo
- **Esquema compartido de la base** (migraciones `0001` y `0002`): casos, documentos, facturas, campos extraídos con confianza y corrección humana, hallazgos con regla y versión, bitácora solo de inserción (un trigger bloquea `UPDATE` y `DELETE`), políticas con fragmentos en pgvector, chat, tablas de negocio y de gobernanza. Diagrama ER en `docs/datos/esquema.md`.
- **Catálogo de reglas:** 20 reglas con versión y política que las sustenta (`datos/reglas/catalogo.yaml`): 14 de facturas (R-001 a R-031) y 6 de registros de clientes (R-101 a R-106).
- **[[tec/data-steward-agentico/tools/validar-reglas|validar_reglas]]:** motor determinista con pruebas unitarias por regla. Normaliza montos, fechas y RFC; detecta duplicados contra la base y texto inyectado (R-030).
- **[[tec/data-steward-agentico/tools/consultar-calidad|consultar_calidad]]:** 13 reglas de calidad sobre facturas, proveedores, clientes, órdenes de compra y pagos, con su umbral (política P-022). La semilla mide el último resultado sobre los datos reales del piloto y simula 5 semanas anteriores.
- **Datos del piloto con resultado esperado:** 74 facturas sintéticas en 4 diseños y 4 formatos (PNG, JPG, PDF y PDF escaneado), cada una con su verdad de referencia y anotación con las clases de FATURA. 39 son de evaluación (11 aceptadas, 17 rechazadas y 11 a revisión humana) y cubren las 14 reglas de facturas, incluida la inyección de instrucciones. Más 10 archivos de registros de clientes para la Historia 2.
- **Casos de la demo:** F-1040, F-1041, F-1042, V-0206 y V-0207 con los mismos IDs y montos que el mockup.
- **Evaluación:** `scripts/evaluar.py` mide aciertos por campo, clasificación (con matriz de confusión y falsos aceptados) y detección por regla; con la verdad de referencia da 100 %.

## Decisiones
- **Precedencia del resultado sugerido:** revisión humana > rechazo > aceptado. Si hay cualquier duda (baja confianza, monto alto, posible duplicado o falta de política), el caso va a revisión aunque también haya un error claro, porque un dato mal leído puede producir un incumplimiento falso. Es lo que muestra F-1042 en el mockup. Detalle en [[tec/data-steward-agentico/agentes/agente-validador|Validador]].
- **Reglas de calidad precalculadas:** en el piloto `consultar_calidad` no ejecuta reglas en vivo, como dice su nota; el último resultado sí se mide sobre los datos cargados para que sea coherente con lo que ve el chat.

## Pendientes
- El modelo de visión que se está probando no devuelve confianza por campo, así que R-003 (umbral de 80 %) no se puede evaluar. Propuesta: [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|confianza por campo y evaluación del modelo de visión]].
- Acordar con el socio formador las políticas reales de la Historia 2 (las actuales son sintéticas).
- Revisar en la sesión de contratos la forma de `FacturaExtraida` y `ResultadoValidacion`.

## Siguiente paso
Conectar `validar_reglas` al grafo de casos con Carlos Delgado y correr la evaluación con la salida real del modelo de visión.
