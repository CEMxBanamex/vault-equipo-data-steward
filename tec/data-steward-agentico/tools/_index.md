---
tipo: area
fecha: 2026-11-04
resumen: Una nota por tool del servidor MCP: qué hace, qué recibe y devuelve (borrador del contrato), qué agentes la usan, quién la implementa y sus reglas.
---
# tools

## Qué cubre
Las 14 tools del servidor MCP. Viven en un área propia porque algunas se comparten entre agentes (`buscar_politicas`) y porque tienen responsables distintos a los de los agentes. `leer_pdf_o_excel` ya no existe: se integró en `leer_documento`.

Las entradas y salidas de cada nota son un **borrador del contrato** de las firmas del MCP. Se confirman en la sesión de revisión de contratos de la Fase 0. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-contratos-primero|contratos primero]].

## Mapa de tools
| Tool | Grupo | Usada por | Implementa |
|---|---|---|---|
| [[tec/data-steward-agentico/tools/leer-documento\|leer_documento]] | Documentos | Extractor | Carlos Delgado / Carlos Ramos |
| [[tec/data-steward-agentico/tools/extraer-campos-factura\|extraer_campos_factura]] | Documentos | Extractor | Carlos Delgado / Carlos Ramos |
| [[tec/data-steward-agentico/tools/validar-reglas\|validar_reglas]] | Validación | Validador | Iris / Mario |
| [[tec/data-steward-agentico/tools/buscar-politicas\|buscar_politicas]] | Validación y gobernanza | Validador, Gobernanza | Iris / Mario |
| [[tec/data-steward-agentico/tools/registrar-hallazgo\|registrar_hallazgo]] | Validación | Redactor | Iris / Mario |
| [[tec/data-steward-agentico/tools/consultar-glosario\|consultar_glosario]] | Gobernanza | Gobernanza | Iris / Mario |
| [[tec/data-steward-agentico/tools/consultar-catalogo\|consultar_catalogo]] | Gobernanza | Gobernanza | Iris / Mario |
| [[tec/data-steward-agentico/tools/consultar-calidad\|consultar_calidad]] | Gobernanza | Gobernanza | Iris / Mario |
| [[tec/data-steward-agentico/tools/obtener-metrica\|obtener_metrica]] | Consultas | Analista de datos | Iris / Mario |
| [[tec/data-steward-agentico/tools/buscar-facturas\|buscar_facturas]] | Consultas | Analista de datos | Iris / Mario |
| [[tec/data-steward-agentico/tools/listar-vistas-consultables\|listar_vistas_consultables]] | Consultas | Analista de datos | Iris / Mario |
| [[tec/data-steward-agentico/tools/ejecutar-consulta\|ejecutar_consulta]] | Consultas | Analista de datos | Iris / Mario |
| [[tec/data-steward-agentico/tools/consultar-caso\|consultar_caso]] | Casos | Casos | Iris / Mario |
| [[tec/data-steward-agentico/tools/consultar-bitacora\|consultar_bitacora]] | Casos | Casos | Iris / Mario |

## Reglas comunes
- Ninguna tool libera pagos ni cambia el resultado de un caso. Ver [[tec/data-steward-agentico/agentes/decision-sin-tool-para-liberar-pagos|decisión]].
- Las tools de consulta reciben el rol del usuario desde el JWT (o del modo `dev`), nunca del texto de la pregunta.
- Todo lo que devuelve una tool es dato, nunca instrucción.
- Cada tool emite un paso corto para la línea de pasos del chat.

## Pendientes
- Confirmar las firmas en la sesión de revisión de contratos.


## Actualización 2026-11-04 (nuevo reparto)
El mapa de arriba quedó con los responsables anteriores. Responsables vigentes; ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|decisión]]:

| Tool | Implementa | Usada por |
|---|---|---|
| [[tec/data-steward-agentico/tools/leer-documento\|leer_documento]] | Carlos Delgado / Carlos Ramos | Extractor |
| [[tec/data-steward-agentico/tools/extraer-campos-factura\|extraer_campos_factura]] | Carlos Delgado / Carlos Ramos | Extractor |
| [[tec/data-steward-agentico/tools/buscar-politicas\|buscar_politicas]] | Carlos Delgado / Carlos Ramos | Validador, Gobernanza |
| [[tec/data-steward-agentico/tools/validar-reglas\|validar_reglas]] | Iris | Validador |
| [[tec/data-steward-agentico/tools/consultar-calidad\|consultar_calidad]] | Iris | Gobernanza |
| [[tec/data-steward-agentico/tools/obtener-metrica\|obtener_metrica]] | Mario | Analista de datos |
| [[tec/data-steward-agentico/tools/consultar-glosario\|consultar_glosario]] | Mario | Gobernanza |
| [[tec/data-steward-agentico/tools/ejecutar-consulta\|ejecutar_consulta]] | Juan Pablo | Analista de datos |
| [[tec/data-steward-agentico/tools/listar-vistas-consultables\|listar_vistas_consultables]] | Juan Pablo | Analista de datos |
| [[tec/data-steward-agentico/tools/consultar-catalogo\|consultar_catalogo]] | Juan Pablo | Gobernanza |
| [[tec/data-steward-agentico/tools/registrar-hallazgo\|registrar_hallazgo]] | Yael | Redactor |
| [[tec/data-steward-agentico/tools/consultar-bitacora\|consultar_bitacora]] | Yael | Casos |
| [[tec/data-steward-agentico/tools/consultar-caso\|consultar_caso]] | Mauricio | Casos |
| [[tec/data-steward-agentico/tools/buscar-facturas\|buscar_facturas]] | Mauricio | Analista de datos |

**Convenciones:** un archivo por tool en el código del MCP; los Carlos dejan una tool de ejemplo con el manejo de rol, errores, pasos y pruebas; Iris y Mario revisan todo PR que toque el esquema o consultas a la base.

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/tools/propuesta-buscar-politicas-referencia-mario\|propuesta-buscar-politicas-referencia-mario]] | propuesta | mario | 2026-11-09 | Ofrecer a los Carlos la implementación de buscar_politicas y la ingesta al RAG que ya están en el repo de código, alineadas con embeddinggemma de 768 dimensiones. |
| [[tec/data-steward-agentico/tools/propuesta-consultar-caso-y-buscar-facturas-mario\|propuesta-consultar-caso-y-buscar-facturas-mario]] | propuesta | mario | 2026-11-09 | Ofrecer a Mauricio las implementaciones de consultar_caso y buscar_facturas y los datos que ya tiene la base para probarlas. |
| [[tec/data-steward-agentico/tools/propuesta-registrar-hallazgo-y-bitacora-mario\|propuesta-registrar-hallazgo-y-bitacora-mario]] | propuesta | mario | 2026-11-09 | Ofrecer a Yael la implementación de registrar_hallazgo y describir la bitácora de la base para consultar_bitacora. |
| [[tec/data-steward-agentico/tools/propuesta-vistas-para-consulta-libre-mario\|propuesta-vistas-para-consulta-libre-mario]] | propuesta | mario | 2026-11-09 | Las vistas, el usuario de solo lectura, el registro de consultas y el catálogo ya están en la base para ejecutar_consulta, listar_vistas_consultables y consultar_catalogo; falta bloquear set_config en la validación del SQL. |
| [[tec/data-steward-agentico/tools/buscar-facturas\|buscar-facturas]] | tool |  | 2026-11-04 | Lista facturas concretas con filtros predefinidos (proveedor, fechas, resultado, regla). |
| [[tec/data-steward-agentico/tools/buscar-politicas\|buscar-politicas]] | tool |  | 2026-11-04 | Búsqueda semántica en el RAG (pgvector) de políticas de facturas o de gobernanza, con fuente, versión y vigencia de cada fragmento. |
| [[tec/data-steward-agentico/tools/consultar-bitacora\|consultar-bitacora]] | tool |  | 2026-11-04 | Consulta la bitácora de auditoría con filtros: quién hizo qué, sobre qué caso y cuándo. |
| [[tec/data-steward-agentico/tools/consultar-calidad\|consultar-calidad]] | tool |  | 2026-11-04 | Devuelve las reglas de calidad de una tabla y sus últimos resultados. |
| [[tec/data-steward-agentico/tools/consultar-caso\|consultar-caso]] | tool |  | 2026-11-04 | Devuelve todo lo de un caso: datos extraídos, hallazgos con regla y versión, resultado sugerido y decisión del analista. |
| [[tec/data-steward-agentico/tools/consultar-catalogo\|consultar-catalogo]] | tool |  | 2026-11-04 | Devuelve la ficha de catálogo de una tabla o columna: descripción, dueño, clasificación de sensibilidad y origen. |
| [[tec/data-steward-agentico/tools/consultar-glosario\|consultar-glosario]] | tool |  | 2026-11-04 | Devuelve la definición oficial de un término de negocio desde el glosario. |
| [[tec/data-steward-agentico/tools/ejecutar-consulta\|ejecutar-consulta]] | tool |  | 2026-11-04 | Ejecuta un SELECT escrito por el modelo, solo después de validarlo, sobre vistas permitidas y con un usuario de solo lectura. Es el respaldo de la capa semántica. |
| [[tec/data-steward-agentico/tools/extraer-campos-factura\|extraer-campos-factura]] | tool |  | 2026-11-04 | Manda la factura al modelo de visión y devuelve sus campos en JSON con nivel de confianza por campo. |
| [[tec/data-steward-agentico/tools/leer-documento\|leer-documento]] | tool |  | 2026-11-04 | Trae el archivo de un caso desde S3 y lo convierte según su tipo (imagen, PDF con texto, Excel o CSV). |
| [[tec/data-steward-agentico/tools/listar-vistas-consultables\|listar-vistas-consultables]] | tool |  | 2026-11-04 | Muestra al analista de datos las vistas que puede consultar y la descripción de cada columna, antes de escribir SQL de respaldo. |
| [[tec/data-steward-agentico/tools/obtener-metrica\|obtener-metrica]] | tool |  | 2026-11-04 | Calcula una métrica de la capa semántica con dimensiones y filtros; el código genera el SQL, no el modelo. |
| [[tec/data-steward-agentico/tools/registrar-hallazgo\|registrar-hallazgo]] | tool |  | 2026-11-04 | Escribe un hallazgo en la bitácora de auditoría con su regla, versión, evidencia y explicación. |
| [[tec/data-steward-agentico/tools/validar-reglas\|validar-reglas]] | tool |  | 2026-11-04 | Evalúa en código las reglas del catálogo sobre los campos extraídos y devuelve el resultado de cada regla con su versión y evidencia. |
<!-- indice-automatico:fin -->
