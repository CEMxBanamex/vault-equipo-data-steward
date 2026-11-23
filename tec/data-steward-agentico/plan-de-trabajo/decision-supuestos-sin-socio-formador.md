---
tipo: decision
fecha: 2026-11-20
autor: juan-pablo
resumen: Sin contacto con el socio formador, el piloto adopta como definitivos los supuestos de datos, reglas y gobernanza, y fundamenta las políticas de facturas en normas públicas del SAT (CFF art. 29-A, Anexo 20 y lista 69-B).
---
# Decisión: supuestos del piloto sin el socio formador

- **Contexto:**
  - No hay contacto con el socio formador, así que las preguntas de `docs/datos/preguntas_socio_formador.md` (repo de código) no se van a contestar. S1-07 esperaba esa respuesta por escrito.
  - Las 14 reglas de facturas y sus políticas (P-001 a P-004, P-011) son sintéticas: están alineadas con México, pero no citan ninguna norma real.
  - Las facturas del piloto no son CFDI: son imágenes y PDF con folio, RFC, subtotal e IVA, pero sin UUID, régimen fiscal, uso de CFDI, forma o método de pago ni tipo de comprobante. Por eso no se pueden verificar contra el SAT.
  - Queda menos de una semana y media para cerrar el proyecto (fin de noviembre).
- **Decisión:** los supuestos de la tabla de abajo pasan a ser definitivos para el piloto, y las políticas de facturas se fundamentan en normas públicas del SAT.
- **Por qué:** el equipo deja de esperar una respuesta que no llegará; el RAG cita normas reales en vez de documentos inventados, y la lista 69-B da una validación con datos públicos reales sin tocar datos del socio formador.
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]], [[tec/data-steward-agentico/tareas/juan-pablo|tareas de Juan Pablo]], [[tec/data-steward-agentico/plan-de-trabajo/propuesta-avance-frente-datos-mario|avance del frente de datos (Mario)]], [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|validaciones deterministas en código]]

## Supuestos adoptados
| # | Pregunta al socio formador | Supuesto definitivo |
|---|---|---|
| 1 | Datos de negocio que se consultan desde el chat | Ciclo de cuentas por pagar (proveedores, órdenes de compra, facturas, pagos y centros de costo), más clientes para la validación de registros |
| 2 | Preguntas típicas de un analista | Las 12 métricas actuales (monto facturado, tasa de rechazo, tiempo promedio de revisión, pagos a tiempo, tasa de conciliación, etc.) |
| 3 | Otros dominios (contratos, tesorería) | Ninguno para el piloto |
| 4 | Reglas de revisión de facturas | Las 14 actuales, con el fundamento de sus políticas cambiado a normas del SAT, más una regla nueva de la lista 69-B (ver abajo) |
| 5 | Monto que exige revisión adicional | 250,000 MXN. Es un criterio interno sin base en el SAT; queda como parámetro del catálogo |
| 6 | Qué hacer con un dato leído con poca confianza | Siempre a revisión humana con confianza menor a 80 %. Criterio conservador, propio de un banco |
| 7 | Registros que se validan contra políticas | Archivos de clientes en CSV o Excel (campos obligatorios, RFC, correo, fecha de alta y unicidad) |
| 8 | Políticas autorizadas para el RAG | No hay. Se usan políticas sintéticas derivadas de normas públicas: SAT para facturas y DAMA-DMBOK para gobernanza |
| 9 | Roles y niveles de clasificación | Los de DAMA: data owner, data steward y custodio. Niveles: pública, interna, confidencial y restringida |
| 10 | Preguntas de gobernanza para la demo | Las 35 preguntas de prueba del agente de gobernanza que preparó Mario |

Todas las políticas siguen marcadas como *documento sintético para el piloto académico*; ahora indican además la norma pública en la que se basan.

## Qué se toma del SAT
| Fuente pública | Uso en el piloto |
|---|---|
| **Código Fiscal de la Federación, art. 29-A** (requisitos de los comprobantes fiscales) | Fundamento de P-001: datos obligatorios (R-001), RFC del emisor y receptor (R-002, R-018) y tipo de documento (R-031) |
| **Anexo 20 de la RMF, guía de llenado del CFDI 4.0, y sus catálogos** | Fundamento de P-002 y P-001: tasas de IVA de 16, 8 y 0 % (R-011), retenciones en el total (R-014), monedas con clave ISO 4217 (R-005) y tipos de comprobante (ingreso, egreso, etc.) para R-031 |
| **Lista del art. 69-B del CFF** (contribuyentes que facturan operaciones simuladas, CSV público) | Regla nueva: emisor en la lista como *definitivo* → rechazo; como *presunto* → revisión humana |

- **La lista 69-B tiene RFC de empresas reales.** La regla puede consultar la lista real, pero los casos de prueba y de demo usan un RFC sintético agregado a una lista de prueba; ninguna factura inventada lleva el RFC de una empresa real.
- Las reglas siguen siendo código determinista en `validar_reglas`; el SAT solo aporta el fundamento y los datos de la lista.

## Alternativas descartadas
- **Convertir las facturas a CFDI (XML con UUID y timbre):** obliga a rehacer el generador de facturas, la extracción con el modelo de visión y la verdad de referencia. No cabe en el tiempo que queda.
- **Servicio de verificación de CFDI del SAT** (UUID, RFC y total → vigente o cancelado): las facturas sintéticas no tienen UUID y siempre saldrían como no encontradas; con facturas reales se rompería la regla de no usar datos reales.
- **Validación de RFC en el portal del SAT:** pide e.firma y captcha; no es un servicio que el sistema pueda consultar.
- **Seguir esperando al socio formador:** no hay contacto y bloquea al frente de datos.

## Tareas que salen de aquí
Se cargan con las tareas de la semana 3 (23 al 27 nov.). IDs y fechas definitivos al cargarlas.

| Responsable | Tarea | Listo cuando |
|---|---|---|
| Mario | Reescribir P-001 y P-002 (y P-011 si aplica) con su fundamento en el CFF art. 29-A y el Anexo 20, como versión nueva, y recargarlas al RAG | Cada sección de las políticas cita el artículo o apartado del SAT que la respalda y las preguntas de evaluación del RAG siguen pasando |
| Iris | Regla de la lista 69-B: tabla con la lista, regla en `catalogo.yaml` con su política, prueba con un RFC sintético en una lista de prueba y caso de demo | `validar_reglas` rechaza un emisor *definitivo*, manda a revisión un *presunto* y las pruebas pasan |
| Juan Pablo | Agregar al final de `docs/datos/preguntas_socio_formador.md` una sección con los supuestos adoptados y el enlace a esta decisión | El documento del repo de código ya no tiene preguntas abiertas |
