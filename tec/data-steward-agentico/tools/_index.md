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
