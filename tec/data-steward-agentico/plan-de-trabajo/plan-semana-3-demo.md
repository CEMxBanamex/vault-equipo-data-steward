---
tipo: plan
fecha: 2026-11-23
autor: juan-pablo
resumen: Plan del 23 al 29 de noviembre - demo lista el martes 24 en dev (flujo de facturas de punta a punta y chat con gobernanza y casos), ensayo el martes a las 20:00, demo el miércoles 25 y cierre del MVP antes del 30.
---
# Plan de la semana 3: demo y cierre

## Contexto
- **Martes 24:** la demo tiene que estar lista. **Ensayo general a las 20:00**, al terminar la clase.
- **Miércoles 25:** sesión de demo.
- **Domingo 29:** MVP completo (el proyecto cierra al terminar noviembre).
- Al 23 de noviembre van 32 de 41 tareas de la semana 1. Las piezas están (datos, 11 de 14 tools, validador, modelo de visión, pantallas con MSW, dev desplegado), pero falta **unirlas**: el grafo de casos con tools reales, el frontend con el backend real y el grafo del chat.
- Las tareas de esta semana están en los archivos de [[tec/data-steward-agentico/tareas/_index|tareas/]], bajo "Semana 3". El estado, en [[tec/data-steward-agentico/tareas/_tablero|el tablero]].

## Qué se muestra el miércoles
**Dentro de la demo:**
1. **Historia 1 de punta a punta en dev** (`dev.cem-steward.online`): subir una factura → extracción con `gemma3:4b` → reglas y políticas → hallazgos explicados → bandeja y detalle → decisión del analista → bitácora. Con 4 facturas preparadas: una correcta, una con total que no cuadra, una con campo faltante y una con un dato de baja confianza.
2. **Chat con pasos visibles:** preguntas de gobernanza (con fuente) y preguntas sobre un caso ("¿por qué se rechazó?"), con la línea de pasos y su resumen.

**Fuera de la demo** (se termina del 26 al 29): analista de datos y consulta libre, intención mixta, Historia 2 (registros en CSV), Cognito y JWT, prod y la regla de la lista 69-B.

**Plan B:** si el lab o la laptop con Ollama fallan el miércoles, la demo corre en local en una laptop (`make up`), y hay un video de respaldo grabado el martes después del ensayo.

## Calendario
| Día | Qué debe quedar |
| --- | --- |
| **Lunes 23** | Contratos aprobados por PR. Contexto del usuario en el MCP (S3-37). Ollama en dev con una sola laptop sirviendo los tres modelos. Datos sintéticos y RAG en `dsa_dev`. Convención de agentes documentada. Facturas de la demo elegidas |
| **Martes 24** | Grafo de casos con tools reales. Endpoints reales y pantallas sin MSW en dev. Grafo del chat mínimo (gobernanza, casos, general y fuera de alcance) con SSE real. Guion. **Corte a las 17:00**, **ensayo general a las 20:00** y video de respaldo al terminar |
| **Miércoles 25** | **Demo.** Comentarios anotados en una sesión del vault |
| **Jueves 26** | Login con Cognito y base privada (movido del 24 para no arriesgar la demo). Supuestos en el documento del socio formador |
| **Viernes 27** | Analista de datos con `obtener_metrica`, `buscar_facturas` y la consulta libre. Políticas con fundamento del SAT. Regla 69-B. Evaluación de gobernanza |
| **Sábado 28** | Evaluaciones (casos de punta a punta, enrutador), prueba de instrucciones inyectadas, pruebas de punta a punta, intención mixta si alcanza, validación del JWT y prod |
| **Domingo 29** | Presentación final, documentación y video de entrega |

## Ruta crítica para el martes
`S3-14` laptop de demo → `S3-02` Ollama en dev → `S3-11` grafo de casos real → `S3-30` endpoints reales → `S3-31` pantallas sin MSW → `S3-05` ensayo.
En paralelo: `S3-15` grafo del chat (no espera a `S3-12`: arranca con la convención de S1-27 y el grafo de casos de S1-28) → `S3-19` gobernanza (también necesita `S3-37`, el contexto del usuario en el MCP) y `S3-35` casos en el chat → `S3-33` SSE real → `S3-34` chat sin MSW → `S3-05` ensayo.

**Corte a las 17:00 del martes:** si a esa hora el chat no responde en dev, el ensayo de las 20:00 y la demo muestran el flujo de casos en dev y el chat en local. Así quedan tres horas para preparar el plan B sin improvisar en el ensayo.

## Tareas de la semana 1 que siguen abiertas
| Tarea | Qué pasa con ella |
|---|---|
| S1-06 Contratos | Cerrada el 23: contratos de tools y SSE congelados en dev; S3-01 queda para los endpoints del chat (PR 18) |
| S1-08 Tools de consulta libre | Se mueve al viernes 27, antes de S3-16 |
| S1-09 Login con Cognito | Se cierra con S3-07 |
| S1-11 Checkpoint del 13 nov. | Cerrada: ya no aplica; la reemplazan S3-05 y S3-06 |
| S1-22 Calibrar RAG y evaluar gobernanza | Se cierra con S3-22 |
| S1-23 Gobernanza en el chat | Se cierra con S3-19 |
| S1-26 Evaluación del modelo de visión | La decisión ya está documentada (92.2 %); Carlos Delgado la puede marcar |
| S1-32 Agente de ejemplo | Se cierra con S3-12 |
| S1-33 Esqueleto del grafo del chat | Se cierra con S3-15 |

## Riesgos
| Riesgo | Mitigación |
|---|---|
| La laptop con Ollama no está encendida o en la tailnet el martes o el miércoles | Acordar quién la tiene encendida; plan B en local |
| Una sola laptop con los tres modelos se queda sin VRAM | Probarlo el lunes (S3-14); si no cabe, el modelo de chat en una segunda laptop y una URL por rol |
| El lab se apaga a media demo | Encenderlo 30 min antes; todo arranca solo. El lab dura 4 horas: encenderlo para el ensayo de las 20:00 y otra vez el miércoles |
| El grafo del chat no llega | Corte de las 17:00 del martes: chat en local |
| Se acaban los créditos del lab | Apagar el lab fuera de las ventanas de integración |

## Enlaces
[[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]] · [[tec/data-steward-agentico/plan-de-trabajo/decision-supuestos-sin-socio-formador|supuestos sin el socio formador]] · [[tec/data-steward-agentico/sesiones/2026-11-22-juan-pablo-despliegue-dev|despliegue de dev]] · [[tec/data-steward-agentico/modelos/decision-modelo-vision-gemma3|modelo de visión]]
