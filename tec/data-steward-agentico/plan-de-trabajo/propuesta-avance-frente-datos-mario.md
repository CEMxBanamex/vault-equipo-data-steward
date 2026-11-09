---
tipo: propuesta
fecha: 2026-11-09
autor: mario
resumen: Registrar en el plan el avance del frente de datos y los supuestos sobre los datos de negocio.
---
# Propuesta: avance del frente de datos en el plan de trabajo

- **Nota que se cambiaría:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]] (Juan Pablo).
- **Qué propongo:**
  - **Fase 0, tablas de negocio, vistas, catálogo, glosario y reglas de calidad en el esquema:** hecho (migraciones `0001` y `0002`).
  - **Fase 1, tarea 1.11 (datos de gobernanza y de negocio y métricas de la capa semántica):** hecho, con un supuesto de dominio (ver abajo).
  - **Tools de Iris y Mario:** `validar_reglas`, `consultar_calidad`, `obtener_metrica` y `consultar_glosario` listas con pruebas.
  - **Datos del piloto y evaluación:** 74 facturas y 10 archivos de registros con resultado esperado, más los scripts de evaluación del pipeline y del RAG. FATURA queda con un convertidor listo; falta descargarlo.
  - **Supuesto sobre los datos de negocio:** ciclo de cuentas por pagar (proveedores, órdenes de compra, facturas, pagos y centros de costo) más clientes. Sigue pendiente confirmarlo con el socio formador.
  - **Tabla de responsables en el índice de tools:** la primera tabla del índice todavía dice "Iris / Mario" en todas las tools; conviene marcarla como histórica.
- **Por qué:** para que el resto del equipo sepa qué ya pueden usar.
- **Estado:** pendiente
