---
tipo: sesion
fecha: 2026-10-28
resumen: Cambio de alcance (sin LSTM, con chat y pasos del agente visibles), reparto del Equipo 1 por frentes, plan por fases según dependencias y Excel de seguimiento.
---
# Sesión 2026-10-28: chat y plan de trabajo

## Qué se hizo
- Se revisó la estructura, arquitectura y objetivo del proyecto en el vault.
- Se incorporó el cambio de alcance del socio formador: sin LSTM, con chat de facturas y un "insight de pensamiento".
- Se definió el chat: por caso y global, con preguntas sobre facturas, políticas y generales; un solo grafo con enrutador por intención.
- Se definió cómo se ven los pasos del agente: línea que cambia, se expande en lista y queda como resumen junto a la respuesta.
- Se repartió el trabajo del Equipo 1 por frentes y se organizó en 5 fases según dependencias.
- Se decidió cómo acordar los contratos y que la validación del JWT en las APIs quede al final.
- Se creó el Excel `Plan_por_fases_Data_Steward.xlsx` (fuera del vault): una hoja por fase, tareas con subtareas plegables, nombre, dependencias y estado.

## Decisiones
- [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm|Se quita la LSTM]]
- [[tec/data-steward-agentico/chat/decision-un-grafo-con-enrutador-por-intencion|Un solo grafo del chat con enrutador por intención]]
- [[tec/data-steward-agentico/chat/decision-pasos-del-agente-visibles|Pasos del agente visibles, breves y con resumen]]
- [[tec/data-steward-agentico/plan-de-trabajo/decision-contratos-primero|Contratos primero, como código]]
- [[tec/data-steward-agentico/plan-de-trabajo/decision-rebanadas-verticales|Reparto por rebanadas verticales]]
- [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|Login con Cognito temprano, JWT en las APIs al final]]

## Áreas nuevas
- [[tec/data-steward-agentico/chat/_index|chat]]: el tema no encajaba en agentes ni en interfaces porque cruza ambos.
- [[tec/data-steward-agentico/plan-de-trabajo/_index|plan-de-trabajo]]: equipo, reparto y fases; no es tema técnico de ninguna área existente.

## Pendientes
- Definir fechas de entrega y revisiones con el socio formador.
- Confirmar la división interna de frontend (casos/bitácora y chat) y de agentes (grafo de casos y grafo del chat).
- Agregar el chat y la pantalla Asistente al mockup.
- Arrancar la Fase 0: entorno local, esquema, prueba de visión y borradores de contratos.

## Siguiente paso
Arrancar la Fase 0. Ver [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]].
