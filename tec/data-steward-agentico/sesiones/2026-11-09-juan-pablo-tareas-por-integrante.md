---
tipo: sesion
fecha: 2026-11-09
autor: juan-pablo
resumen: Plan de la semana 1 (9 al 13 nov.) y sistema de tareas por integrante con publicación automática y tablero generado.
---
# Sesión 2026-11-09: tareas por integrante y plan de la semana 1

## Qué se hizo
- Se revisó el estado del proyecto contra el calendario: todo debe quedar antes de que acabe noviembre, en tres semanas, con el lunes 16 feriado. Meta propuesta: semana 1, cerrar la Fase 0 y arrancar la Fase 1; semana 2, terminar la Fase 1 y hacer la Fase 2 con el primer despliegue; semana 3, chat, evaluación y demo.
- Se armó el plan de la semana 1 con el hito de la revisión de contratos el miércoles 11 y un checkpoint el viernes 13.
- El frente de datos va adelantado: según las sesiones de Mario, esquema, vistas con seguridad por fila, datos, catálogo, glosario, métricas y cuatro tools ya están hechos. Esas tareas se cargaron como listas.
- Se creó el área [[tec/data-steward-agentico/tareas/_index|tareas]] con un archivo por integrante y 41 tareas de la semana 1.
- En el repo: `scripts/tareas.py`, `scripts/generar_tablero.py` y `scripts/publicar_tareas.py`; validación de tareas en `validar_vault.py`; `novedades` ignora `tareas/`; `sincronizar.yml` corre cada 15 minutos; `CODEOWNERS` con el dueño de cada archivo de tareas.

## Decisiones
- [[tec/data-steward-agentico/plan-de-trabajo/decision-tareas-por-integrante|Tareas por integrante y tablero generado]]

## Pendientes
- Que Iris confirme las tareas que se marcaron como listas a partir de la sesión de Mario.
- Integrar en el plan de trabajo la [[tec/data-steward-agentico/plan-de-trabajo/propuesta-avance-frente-datos-mario|propuesta de avance del frente de datos]].
- Avisar al equipo cómo marcar sus tareas.

## Siguiente paso
Subir los cambios del repo, revisar el primer tablero en `main` y arrancar la semana con las tareas que vencen el martes 10.
