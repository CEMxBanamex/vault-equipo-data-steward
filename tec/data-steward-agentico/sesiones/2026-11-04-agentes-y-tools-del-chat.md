---
tipo: sesion
fecha: 2026-11-04
resumen: Requerimiento de gobernanza y consultas en el chat; se eligió el enrutador por dominio con tres agentes, intención mixta, tools específicas y capa semántica; Excel actualizado.
---
# Sesión 2026-11-04: agentes y tools del chat

## Qué se hizo
- Se revisaron los casos de uso: solo están documentadas las dos historias (facturas y validación con políticas); si el socio formador pasó más, no están en el vault.
- Se incorporó el requerimiento de que el chat resuelva dudas de gobernanza de datos y consultas a la base de negocio y facturas.
- Se compararon cuatro diseños de agentes y tres de tools.
- Se eligió el enrutador por dominio con intención mixta, tools específicas y capa semántica con SQL validado de respaldo.
- Se actualizó el Excel `Plan_por_fases_Data_Steward.xlsx`: 41 tareas y 157 subtareas.

## Decisiones
- [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|Enrutador por dominio, tools específicas y capa semántica]]

## Pendientes
- Confirmar con el socio formador qué datos de negocio esperan consultar.
- Revisar la carga del frente de datos de Iris y Mario.
- Definir las métricas y dimensiones de la capa semántica.

## Siguiente paso
Arrancar la Fase 0, incluida la prueba rápida de text-to-SQL. Ver [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]].


## Actualización (notas por agente y por tool)
- Se crearon las 7 notas de agentes en [[tec/data-steward-agentico/agentes/_index|agentes]] y el área nueva [[tec/data-steward-agentico/tools/_index|tools]] con las 14 tools, enlazadas entre sí. Las tools viven aparte porque `buscar_politicas` se comparte entre dos agentes.
