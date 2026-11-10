---
tipo: sesion
fecha: 2026-11-09
autor: iris
resumen: Validador como nodo de código con cita exacta por hallazgo, corrección del filtro de buscar_politicas, R-003 sin confianza y evaluación del validador (39/39).
---
# Sesión 2026-11-09 (tarde): validador

Trabajo en pareja con Mario; su sesión de la tarde cubre el agente de gobernanza y la seguridad por fila. Código en el repo de código, rama `datos/fases-0-a-4`.

## Qué se hizo
- **Cita exacta en cada hallazgo** desde el catálogo de reglas, sin depender del RAG. Ver [[tec/data-steward-agentico/tools/validar-reglas|validar_reglas]].
- **Nodo determinista del validador** (`preparar_para_redactor`) y prompt alterno con LLM. Ver [[tec/data-steward-agentico/agentes/agente-validador|validador]].
- **Hallazgo:** filtrar por `tipo=facturas` dejaba sin política a R-002 y a la Historia 2. Se busca por regla e historia.
- **R-003 sin confianza:** ahora avisa; el efecto se configura en el catálogo. Ver [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|propuesta de confianza]].
- **Evaluación del validador:** `scripts/evaluar_validador.py` (`citas`, `entradas`, `respuestas`). 20/20 reglas con su sección; 39/39 casos, sin falsos aceptados.

## Decisiones
- La cita (política, versión y sección) la pone el código; el RAG solo trae el texto. Si el RAG no lo encuentra, se usa la cita del catálogo y el paso lo dice.

## Pendientes
- Acordar con Carlos Delgado si el validador queda como nodo de código.
- Decidir el efecto de R-003 cuando no hay confianza.

## Siguiente paso
Conectar `validar_reglas` y `preparar_para_redactor` al grafo de casos con Carlos Delgado.
