---
tipo: decision
fecha: 2026-11-04
autor: juan-pablo
resumen: Iris y Mario se enfocan en la estructura y los datos de la base; las 14 tools se reparten entre todo el equipo y los agentes se construyen en dos subequipos, uno por grafo.
---
# Decisión: reparto de tools y subequipos de agentes

- **Contexto:** Iris y Mario tenían 12 de las 14 tools además de todo lo de la base de datos. Ellos se ofrecieron para la estructura de la base y la generación de datos, no para casi todas las tools.
- **Decisión 1, frente de Iris y Mario = la base de datos:**
  - Estructura: esquema, migraciones, vistas consultables y seguridad por fila sobre las vistas.
  - Datos del piloto (FATURA, casos con errores y resultados esperados) y datos de negocio sintéticos.
  - Contenido de gobernanza: catálogo, glosario, políticas sintéticas, reglas de calidad y resultados.
  - Definiciones: catálogo de reglas y métricas de la capa semántica.
  - Ingesta al RAG y datos de evaluación.
- **Decisión 2, reparto de tools** (cada quien toma tools cercanas a lo que ya construye):

| Persona | Tools |
|---|---|
| Iris | `validar_reglas`, `consultar_calidad` |
| Mario | `obtener_metrica`, `consultar_glosario` |
| Carlos Delgado / Carlos Ramos | `leer_documento`, `extraer_campos_factura`, `buscar_politicas` |
| Juan Pablo | `ejecutar_consulta`, `listar_vistas_consultables`, `consultar_catalogo` |
| Yael | `registrar_hallazgo`, `consultar_bitacora` |
| Mauricio | `consultar_caso`, `buscar_facturas` |

- **Decisión 3, orden:** primero tools y después agentes, pero solapado: contratos en la Fase 0; en las Fases 1 y 2 cada quien hace sus tools mientras los Carlos montan el servidor MCP base, la plantilla de tool y el esqueleto de los grafos con tools falsas; los subequipos conectan las tools reales conforme salen.
- **Decisión 4, subequipos por grafo** (cada agente tiene un dueño que lleva su prompt, pruebas y evaluación):

| Grafo | Líder | Agente | Dueño | Apoyo |
|---|---|---|---|---|
| Casos | Carlos Delgado | Extractor de documentos | Carlos Delgado | Carlos Ramos |
| Casos | Carlos Delgado | Validador | Iris | Carlos Delgado |
| Casos | Carlos Delgado | Redactor de hallazgos | Yael | Carlos Delgado |
| Chat | Carlos Ramos | Enrutador e intención mixta | Carlos Ramos | — |
| Chat | Carlos Ramos | Gobernanza | Mario | Iris, Juan Pablo |
| Chat | Carlos Ramos | Analista de datos | Carlos Ramos | Juan Pablo, Mario, Mauricio |
| Chat | Carlos Ramos | Casos | Mauricio | Yael |

- **Condiciones:**
  - El esquema es contrato de la Fase 0; cada dueño de tool revisa que las tablas tengan lo que necesita.
  - Iris y Mario revisan todo PR que toque el esquema o consultas a la base.
  - Los Carlos dejan una tool de ejemplo y un agente de ejemplo con la convención (rol, errores, pasos y pruebas); el resto copia ese patrón.
  - Un archivo por tool en el código del MCP para evitar conflictos.
- **Por qué:** balancea la carga (nadie con más de 3 tools), cada tool va con quien consume sus datos, todo el equipo aprende el MCP y LangGraph, y el agente más difícil (analista de datos) queda con Carlos Ramos con el apoyo de los dueños de sus tools. Juan Pablo solo apoya agentes porque en la Fase 3 tiene el despliegue en AWS.
- **Alternativas descartadas:** Iris y Mario con casi todas las tools; construir todas las tools antes de empezar los agentes (los agentes empezarían tarde y los riesgos se descubrirían al final).
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]], [[tec/data-steward-agentico/tools/_index|tools]], [[tec/data-steward-agentico/agentes/_index|agentes]]
