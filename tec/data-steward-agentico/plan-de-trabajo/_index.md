---
tipo: area
fecha: 2026-10-28
resumen: Organización del Equipo 1: integrantes, reparto por frentes, plan por fases según dependencias, contratos y ruta crítica.
---
# plan-de-trabajo

## Equipo y reparto
| Frente | Integrantes |
|---|---|
| Infraestructura y CI/CD | Juan Pablo Pérez Gutiérrez |
| Datos, reglas y tools de datos | Iris Giselle Balderas Arreola, Mario Oropeza Pérez |
| Agentes y modelos | Carlos Manuel Delgado Vázquez, Carlos Manuel Ramos Gastélum |
| Frontend | Yael Michel García López, Mauricio Guerrero González |

- **Infraestructura y CI/CD:** AWS, contenedores, Tailscale, pipelines y autenticación.
- **Datos (Iris y Mario):** esquema, migraciones, datos del piloto, políticas sintéticas, ingesta al RAG, catálogo de reglas, tools de datos del MCP (`validar_reglas`, `buscar_politicas`, `registrar_hallazgo`, `consultar_caso`, `buscar_facturas`), endpoint de políticas, calidad del RAG y evaluación.
- **Agentes y modelos:** grafos de casos y del chat, prompts, streaming de pasos, servidor MCP base, tools de documentos y visión, modelos en las laptops.
- **Frontend:** pantallas, chat, línea de pasos, subida a S3 y los endpoints de sus pantallas.
- Hay dos Carlos Manuel: en la documentación se identifican por apellido (Delgado y Ramos).
- Sugerencia pendiente de confirmar: dividir frontend en casos/bitácora y chat, y agentes en grafo de casos y grafo del chat, para no chocar en los PRs.

## Fases
| Fase | Nombre | Qué pasa |
|---|---|---|
| 0 | Cimientos y contratos | Entorno local, CI mínimo, esquema, datos del piloto, prueba de visión, base del frontend y contratos acordados |
| 1 | Piezas por separado con datos falsos | Cada equipo construye contra los contratos: MSW en frontend, tools falsas en agentes, eventos SSE simulados; datos reales y AWS base en paralelo |
| 2 | Integración del flujo de casos | RAG, tools de datos reales, grafo conectado, endpoints de casos, login con Cognito y prueba de punta a punta en local |
| 3 | Chat y despliegue | Tools y grafo del chat, streaming de pasos, pantallas del chat y despliegue completo en AWS con acceso restringido por IP |
| 4 | Autenticación, evaluación y demo | JWT en las APIs, evaluación contra casos de referencia, ajuste de prompts, pruebas y demo |

- **Ruta crítica:** contratos → prueba de visión → grafo de casos → integración → chat → evaluación.
- La prueba del modelo de visión va en la Fase 0 porque es el mayor riesgo técnico: si falla, se activa el plan B con Bedrock.
- El primer despliegue real en AWS va al terminar la Fase 2, no al final.
- **Plan detallado:** Excel `Plan_por_fases_Data_Steward.xlsx` (fuera del vault), con 39 tareas y 127 subtareas, una hoja por fase, nombre, dependencias y estado (Pendiente, En proceso, Completado).

## Notas
- [[tec/data-steward-agentico/plan-de-trabajo/decision-contratos-primero|Decisión: contratos primero, como código]]
- [[tec/data-steward-agentico/plan-de-trabajo/decision-rebanadas-verticales|Decisión: reparto por rebanadas verticales]]
- [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|Decisión: login con Cognito temprano, JWT en las APIs al final]]

## Pendientes
- Definir fechas de entrega y revisiones con el socio formador para ponerle semanas a cada fase.
- Confirmar la división interna de frontend y de agentes.


## Actualización 2026-11-04
- El plan creció a 41 tareas y 157 subtareas por el requerimiento de gobernanza y consultas:
  - **Fase 0:** tablas de negocio, vistas, catálogo, glosario y reglas de calidad en el esquema; prueba rápida de text-to-SQL con el modelo local.
  - **Fase 1:** tarea 1.11, datos de gobernanza y de negocio, y definición de métricas de la capa semántica (Iris y Mario); tarea 1.12, esqueleto del grafo del chat (los Carlos).
  - **Fase 3:** tools de casos y gobernanza (3.1), capa semántica y consultas seguras (3.9) y grafo del chat con los tres agentes e intención mixta (3.3).
  - **Fase 4:** evaluación del enrutador y de las consultas.
- El frente de datos de Iris y Mario creció bastante: conviene revisar si necesitan apoyo en la Fase 3.

- [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|Decisión: vault compartido del equipo]] (2026-11-04)


## Actualización 2026-11-04 (reparto de tools y subequipos)
- [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|Decisión: reparto de tools y subequipos de agentes]]
- **Iris y Mario:** su frente es la base de datos (estructura, datos del piloto y de negocio, contenido de gobernanza, definiciones de reglas y métricas, ingesta al RAG y datos de evaluación) más 2 tools cada uno.
- **Tools:** repartidas entre los 7; nadie tiene más de 3.
- **Agentes:** dos subequipos. Carlos Delgado lidera el grafo de casos y Carlos Ramos el del chat; cada agente tiene un dueño. Esto resuelve la división interna de los Carlos que estaba pendiente.
- **Siguen pendientes:** dividir con nombre individual las subtareas de frontend entre Yael y Mauricio, y actualizar el Excel y `CODEOWNERS` con el nuevo reparto.

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/plan-de-trabajo/decision-contratos-primero\|decision-contratos-primero]] | decision |  | 2026-10-28 | En la Fase 0 se acuerdan los contratos (esquema, firmas de tools, endpoints y eventos SSE) como código, para que cada equipo trabaje en paralelo con datos falsos. |
| [[tec/data-steward-agentico/plan-de-trabajo/decision-rebanadas-verticales\|decision-rebanadas-verticales]] | decision |  | 2026-10-28 | Cada equipo es dueño de su función de punta a punta: el frontend hace los endpoints de sus pantallas, agentes entrega funciones de Python y datos es dueño de las tools que leen y escriben la base. |
| [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes\|decision-reparto-de-tools-y-subequipos-de-agentes]] | decision | juan-pablo | 2026-11-04 | Iris y Mario se enfocan en la estructura y los datos de la base; las 14 tools se reparten entre todo el equipo y los agentes se construyen en dos subequipos, uno por grafo. |
| [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo\|decision-vault-compartido-del-equipo]] | decision | juan-pablo | 2026-11-04 | El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas. |
| [[tec/data-steward-agentico/plan-de-trabajo/decision-tareas-por-integrante\|decision-tareas-por-integrante]] | decision | juan-pablo | 2026-11-09 | Las tareas viven en un archivo por integrante dentro de tareas/, que solo marca su dueño y se publica en main sin PR; un Action genera el tablero del equipo. |
| [[tec/data-steward-agentico/plan-de-trabajo/propuesta-avance-frente-datos-mario\|propuesta-avance-frente-datos-mario]] | propuesta | mario | 2026-11-09 | Registrar en el plan el avance del frente de datos y los supuestos sobre los datos de negocio. |
<!-- indice-automatico:fin -->
