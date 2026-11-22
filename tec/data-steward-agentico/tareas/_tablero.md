---
tipo: tablero
fecha: 2026-11-21
autor: vault-bot
resumen: Estado de las tareas del equipo (hitos, bloqueos, vencidas, lo próximo y el avance por persona). Léelo al empezar.
---
# Tablero de tareas

_Lo genera GitHub Actions a partir de los archivos de `tareas/`. No lo edites a mano: marca tus tareas en tu archivo. Cómo funciona: [[tec/data-steward-agentico/tareas/_index|tareas]]._

**Actualizado:** 2026-11-21 (Ciudad de México). **Semana en curso:** Semana 1 · 9 al 13 nov.

**Avance general:** 26 de 41 listas (63 %) · 2 en proceso · 1 bloqueadas · 12 pendientes.

## Hitos
| Hito | Responsable | Vence | Estado |
|---|---|---|---|
| **S1-06** Sesión de revisión de contratos y PR aprobado a main | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 11/11 | Pendiente |
| **S1-11** Checkpoint del viernes (30 min) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |

## Bloqueadas
| Tarea | Responsable | Motivo |
|---|---|---|
| **S1-23** Conectar el agente de gobernanza al grafo del chat | [[tec/data-steward-agentico/tareas/mario\|Mario]] | el grafo del chat no existe aún; espera S1-33 y S1-32 (carlos-ramos) |

## Vencidas
| Tarea | Responsable | Venció | Estado |
|---|---|---|---|
| **S1-05** Infra en AWS: RDS PostgreSQL con pgvector y EC2 | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 10/11 | Pendiente |
| **S1-30** Borrador de los eventos SSE del chat | [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 10/11 | Pendiente |
| **S1-06** Sesión de revisión de contratos y PR aprobado a main | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 11/11 | Pendiente |
| **S1-07** Confirmar con el socio formador los datos de negocio | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 11/11 | Pendiente |
| **S1-26** Evaluación controlada del modelo de visión y decisión: local o Bedrock | [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | 11/11 | En proceso |
| **S1-31** Prueba rápida de text-to-SQL con el modelo local | [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 11/11 | Pendiente |
| **S1-32** Agente de ejemplo con la convención | [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 12/11 | Pendiente |
| **S1-08** Primera versión de ejecutar_consulta, listar_vistas_consultables y consultar_catalogo | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |
| **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |
| **S1-10** Pipeline de imágenes a ECR | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |
| **S1-11** Checkpoint del viernes (30 min) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | Pendiente |
| **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales | [[tec/data-steward-agentico/tareas/mario\|Mario]] | 13/11 | En proceso |
| **S1-23** Conectar el agente de gobernanza al grafo del chat | [[tec/data-steward-agentico/tareas/mario\|Mario]] | 13/11 | Bloqueado |
| **S1-33** Esqueleto del grafo del chat con tools falsas | [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 13/11 | Pendiente |
| **S1-40** Primera versión de consultar_caso y buscar_facturas | [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | 13/11 | Pendiente |

## Vencen hoy y mañana
_Nada vence hoy ni mañana._

## Se destrabaron
_Pendientes cuyas dependencias ya están listas: se pueden empezar._

| Tarea | Responsable | Vence | Dependía de |
|---|---|---|---|
| **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | S1-35 |
| **S1-10** Pipeline de imágenes a ECR | [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 13/11 | S1-01 |

## Avance por frente
| Frente | Listas | En proceso | Bloqueadas | Pendientes | Avance |
|---|---|---|---|---|---|
| Infraestructura y CI/CD | 4 | 0 | 0 | 7 | ▓▓▓▓░░░░░░ 36 % |
| Datos | 10 | 1 | 1 | 0 | ▓▓▓▓▓▓▓▓░░ 83 % |
| Agentes y modelos | 5 | 1 | 0 | 4 | ▓▓▓▓▓░░░░░ 50 % |
| Frontend | 7 | 0 | 0 | 1 | ▓▓▓▓▓▓▓▓▓░ 88 % |

## Avance por persona
| Persona | Listas | En proceso | Bloqueadas | Pendientes | Avance | Lo siguiente |
|---|---|---|---|---|---|---|
| [[tec/data-steward-agentico/tareas/juan-pablo\|Juan Pablo]] | 4 | 0 | 0 | 7 | ▓▓▓▓░░░░░░ 36 % | **S1-05** Infra en AWS: RDS PostgreSQL con pgvector y EC2 |
| [[tec/data-steward-agentico/tareas/iris\|Iris]] | 6 | 0 | 0 | 0 | ▓▓▓▓▓▓▓▓▓▓ 100 % | — |
| [[tec/data-steward-agentico/tareas/mario\|Mario]] | 4 | 1 | 1 | 0 | ▓▓▓▓▓▓▓░░░ 67 % | **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales |
| [[tec/data-steward-agentico/tareas/carlos-delgado\|Carlos Delgado]] | 4 | 1 | 0 | 0 | ▓▓▓▓▓▓▓▓░░ 80 % | **S1-26** Evaluación controlada del modelo de visión y decisión: local o Bedrock |
| [[tec/data-steward-agentico/tareas/carlos-ramos\|Carlos Ramos]] | 1 | 0 | 0 | 4 | ▓▓░░░░░░░░ 20 % | **S1-30** Borrador de los eventos SSE del chat |
| [[tec/data-steward-agentico/tareas/yael\|Yael]] | 5 | 0 | 0 | 0 | ▓▓▓▓▓▓▓▓▓▓ 100 % | — |
| [[tec/data-steward-agentico/tareas/mauricio\|Mauricio]] | 2 | 0 | 0 | 1 | ▓▓▓▓▓▓▓░░░ 67 % | **S1-40** Primera versión de consultar_caso y buscar_facturas |
