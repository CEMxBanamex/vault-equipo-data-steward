---
tipo: sesion
fecha: 2026-11-09
autor: mario
resumen: Prompt y 35 preguntas de prueba del agente de gobernanza, cierre del hueco de set_config en la seguridad por fila y calibración del umbral del RAG.
---
# Sesión 2026-11-09 (tarde): agente de gobernanza y seguridad

Trabajo en pareja con Iris; su sesión de la tarde cubre el validador. Código en el repo de código, rama `datos/fases-0-a-4`.

## Qué se hizo
- **Agente de gobernanza:** prompt (`datos/agentes/gobernanza.md`), 35 preguntas de prueba con fuente esperada y `scripts/evaluar_gobernanza.py`. Ver [[tec/data-steward-agentico/agentes/agente-de-gobernanza|agente de gobernanza]].
- **Seguridad por fila:** se confirmó que `set_config` dentro de un SELECT se salta el filtro. Migración `0003` y `fijar_en_bd` con `SET LOCAL`. Ver [[tec/data-steward-agentico/tools/propuesta-vistas-para-consulta-libre-mario|propuesta para Juan Pablo]].
- **Archivos sintéticos:** el parche del 4 nov. dañaba los PDF y el CSV ilegible de V-0206 (git los trataba como texto). Se restauraron y `.gitattributes` los marca como binarios.
- **RAG:** modo `--calibrar` y 6 preguntas sin política. Ver [[tec/data-steward-agentico/tools/propuesta-buscar-politicas-referencia-mario|propuesta de buscar_politicas]].
- **Para la sesión de contratos y el socio formador:** `docs/datos/sesion_contratos.md` (11 puntos) y `docs/datos/preguntas_socio_formador.md`.
- Pruebas: 227, todas pasan con PostgreSQL + pgvector.

## Pendientes
- Correr `evaluar_rag.py --calibrar` y `evaluar_gobernanza.py respuestas` con los modelos reales.
- Confirmar con el socio formador los datos de negocio.

## Siguiente paso
Sesión de contratos y conexión del agente de gobernanza al grafo del chat con Carlos Ramos.
