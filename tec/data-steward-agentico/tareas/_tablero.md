---
tipo: tablero
fecha: 2026-11-24
autor: vault-bot
resumen: Estado de las tareas del equipo (hitos, bloqueos, vencidas, lo próximo y el avance por persona). Léelo al empezar.
---
# Tablero de tareas

_Lo genera GitHub Actions a partir de los archivos de `tareas/`. No lo edites a mano: marca tus tareas en tu archivo. Cómo funciona: [[tec/data-steward-agentico/tareas/_index|tareas]]._

**Actualizado:** 2026-11-24 (Ciudad de México). **Semana en curso:** Semana 3 · 23 al 29 nov.

**Avance general:** 47 de 79 listas (59 %) · 2 en proceso · 3 bloqueadas · 27 pendientes.

## Hitos
| Hito | Responsable | Vence | Estado |
|---|---|---|---|
| **S1-06** Sesión de revisión de contratos y PR aprobado a main | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 11/11 | Listo |
| **S1-11** Checkpoint del viernes (30 min) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Listo |
| **S3-05** Ensayo general de la demo en dev | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 24/11 | Pendiente |
| **S3-06** Demo del miércoles | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 25/11 | Pendiente |
| **S3-28** Presentación final y entrega | [[tec/data-steward-agentico/tareas/iris\|Iris]] | 29/11 | Pendiente |

## Bloqueadas
| Tarea | Responsable | Motivo |
|---|---|---|
| **S1-23** Conectar el agente de gobernanza al grafo del chat | [[tec/data-steward-agentico/tareas/mario\|Mario]] | el grafo del chat no existe aún; espera S1-33 y S1-32 (carlos-ramos) |
| **S3-19** Agente de gobernanza en el chat para la demo (cierra S1-23) | [[tec/data-steward-agentico/tareas/mario\|Mario]] | espera el grafo del chat (S3-15, carlos-ramos) y el contexto del usuario en el MCP (S3-37, carlos-delgado); el prompt y las tools ya están en dev |
| **S3-22** Evaluar las respuestas del agente de gobernanza (cierra S1-22) | [[tec/data-steward-agentico/tareas/mario\|Mario]] | espera la laptop de demo con el modelo de chat (S3-14, carlos-ramos) |

## Vencidas
| Tarea | Responsable | Venció | Estado |
|---|---|---|---|
| **S1-26** Evaluación controlada del modelo de visión y decisión: local o Bedrock | [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | 11/11 | En proceso |
| **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |
| **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales | [[tec/data-steward-agentico/tareas/mario\|Mario]] | 13/11 | En proceso |
| **S1-23** Conectar el agente de gobernanza al grafo del chat | [[tec/data-steward-agentico/tareas/mario\|Mario]] | 13/11 | Bloqueado |
| **S3-01** Aprobar los contratos por PR (cierra S1-06) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 23/11 | Pendiente |
| **S3-37** Contexto del usuario en el servidor MCP (PR 19 del repo de código) | [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | 23/11 | Pendiente |

## Vencen hoy y mañana
| Tarea | Responsable | Vence | Estado |
|---|---|---|---|
| **S3-05** Ensayo general de la demo en dev | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | hoy | Pendiente |
| **S3-11** Grafo de casos con tools reales y gemma3:4b | [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | hoy | Pendiente |
| **S3-15** Grafo del chat mínimo para la demo (cierra S1-33) | [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | hoy | Pendiente |
| **S3-19** Agente de gobernanza en el chat para la demo (cierra S1-23) | [[tec/data-steward-agentico/tareas/mario\|Mario]] | hoy | Bloqueado |
| **S3-25** Video de respaldo de la demo | [[tec/data-steward-agentico/tareas/iris\|Iris]] | hoy | Pendiente |
| **S3-29** Prompt y pruebas del agente redactor | [[tec/data-steward-agentico/tareas/yael\|Yael]] | hoy | Pendiente |
| **S3-30** Endpoints reales de casos y bitácora | [[tec/data-steward-agentico/tareas/yael\|Yael]] | hoy | Pendiente |
| **S3-31** Pantallas de casos y bitácora sin MSW en dev | [[tec/data-steward-agentico/tareas/yael\|Yael]] | hoy | Pendiente |
| **S3-34** Chat sin MSW en dev | [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | hoy | Pendiente |
| **S3-35** Agente de casos en el chat | [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | hoy | Pendiente |
| **S3-06** Demo del miércoles | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | mañana | Pendiente |

## Se destrabaron
_Pendientes cuyas dependencias ya están listas: se pueden empezar._

| Tarea | Responsable | Vence | Dependía de |
|---|---|---|---|
| **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | S1-35 |
| **S3-34** Chat sin MSW en dev | [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | 24/11 | S3-33 |
| **S1-08** Primera versión de ejecutar_consulta, listar_vistas_consultables y consultar_catalogo | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 27/11 | S1-06, S1-27 |

## Avance por frente
| Frente | Listas | En proceso | Bloqueadas | Pendientes | Avance |
|---|---|---|---|---|---|
| Infraestructura y CI/CD | 12 | 0 | 0 | 9 | ▓▓▓▓▓▓░░░░ 57 % |
| Datos | 15 | 1 | 3 | 3 | ▓▓▓▓▓▓▓░░░ 68 % |
| Agentes y modelos | 11 | 1 | 0 | 8 | ▓▓▓▓▓▓░░░░ 55 % |
| Frontend | 9 | 0 | 0 | 7 | ▓▓▓▓▓▓░░░░ 56 % |

## Avance por persona
| Persona | Listas | En proceso | Bloqueadas | Pendientes | Avance | Lo siguiente |
|---|---|---|---|---|---|---|
| [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 12 | 0 | 0 | 9 | ▓▓▓▓▓▓░░░░ 57 % | **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) |
| [[tec/data-steward-agentico/tareas/iris\|Iris]] | 9 | 0 | 0 | 3 | ▓▓▓▓▓▓▓▓░░ 75 % | **S3-25** Video de respaldo de la demo |
| [[tec/data-steward-agentico/tareas/mario\|Mario]] | 6 | 1 | 3 | 0 | ▓▓▓▓▓▓░░░░ 60 % | **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales |
| [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | 5 | 1 | 0 | 4 | ▓▓▓▓▓░░░░░ 50 % | **S1-26** Evaluación controlada del modelo de visión y decisión: local o Bedrock |
| [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 6 | 0 | 0 | 4 | ▓▓▓▓▓▓░░░░ 60 % | **S3-15** Grafo del chat mínimo para la demo (cierra S1-33) |
| [[tec/data-steward-agentico/tareas/yael\|Yael]] | 5 | 0 | 0 | 4 | ▓▓▓▓▓▓░░░░ 56 % | **S3-29** Prompt y pruebas del agente redactor |
| [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | 4 | 0 | 0 | 3 | ▓▓▓▓▓▓░░░░ 57 % | **S3-34** Chat sin MSW en dev |
