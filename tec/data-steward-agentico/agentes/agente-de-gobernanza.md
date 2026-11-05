---
tipo: agente
fecha: 2026-11-04
resumen: Agente del chat que responde dudas de gobernanza de datos: políticas, términos de negocio, dueños, clasificación de sensibilidad y calidad.
---
# Agente: Gobernanza

- **Grafo:** chat. Lo llama el [[tec/data-steward-agentico/agentes/agente-enrutador|Enrutador]].
- **Ejemplos:** "¿Quién es el dueño de los datos de proveedores?", "¿El RFC es dato sensible?", "¿Qué reglas de calidad aplican a la tabla de facturas?", "¿Qué significa factura conciliada?".
- **Tools:**
  - [[tec/data-steward-agentico/tools/buscar-politicas|buscar_politicas]] (tipo `gobernanza`)
  - [[tec/data-steward-agentico/tools/consultar-glosario|consultar_glosario]]
  - [[tec/data-steward-agentico/tools/consultar-catalogo|consultar_catalogo]]
  - [[tec/data-steward-agentico/tools/consultar-calidad|consultar_calidad]]
- **Regla clave:** cada respuesta cita su fuente (política y versión, término del glosario o ficha del catálogo); si no hay fuente, lo dice.
- **Construye:** Carlos Delgado / Carlos Ramos (las tools, Iris y Mario).
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo del chat, liderado por Carlos Ramos.
- **Dueño:** Mario (prompt, pruebas y evaluación). **Apoyo:** Iris y Juan Pablo.
- **Tools y sus responsables:** `consultar_glosario` (Mario), `consultar_calidad` (Iris), `consultar_catalogo` (Juan Pablo), `buscar_politicas` (Carlos Delgado / Carlos Ramos).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
