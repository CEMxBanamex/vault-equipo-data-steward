---
tipo: tool
fecha: 2026-11-04
resumen: Ejecuta un SELECT escrito por el modelo, solo después de validarlo, sobre vistas permitidas y con un usuario de solo lectura. Es el respaldo de la capa semántica.
---
# Tool: ejecutar_consulta

- **Qué hace:** valida y ejecuta SQL generado por el analista de datos cuando la pregunta no encaja en una métrica ni en `buscar_facturas`.
- **Recibe:** texto SQL y la pregunta original (para el registro).
- **Devuelve:** filas (con límite), columnas y el SQL ejecutado; si la validación falla, el motivo.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]]. Última opción.
- **Implementa:** Iris / Mario. El usuario de base de datos de solo lectura lo configura Juan Pablo.
- **Paso:** "Consulta libre validada…", con el SQL como detalle.
- **Capas de seguridad:**
  - Validación con `sqlglot`: un solo SELECT, solo vistas permitidas, límite de filas obligatorio.
  - Usuario de base de datos de solo lectura con permiso solo sobre las vistas y tiempo máximo por consulta.
  - Seguridad a nivel de fila por rol.
- **Mejora continua:** registra la pregunta y el SQL; las preguntas que se repiten se vuelven métricas nuevas en `obtener_metrica`.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]], [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]]


## Actualización 2026-11-04
- **Implementa:** Juan Pablo (antes Iris / Mario), junto con el usuario de solo lectura, la validación del SQL y la seguridad por fila. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
