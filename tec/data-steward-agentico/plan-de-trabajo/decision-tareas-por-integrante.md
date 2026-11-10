---
tipo: decision
fecha: 2026-11-09
autor: juan-pablo
resumen: Las tareas viven en un archivo por integrante dentro de tareas/, que solo marca su dueño y se publica en main sin PR; un Action genera el tablero del equipo.
---
# Decisión: tareas por integrante y tablero generado

- **Contexto:** el proyecto debe quedar completo antes de que acabe noviembre (tres semanas). El equipo necesitaba ver qué le toca a cada quien y marcar su avance. El plan detallado vive en un Excel fuera del vault, que nadie consulta a diario y que los asistentes de IA no leen.
- **Decisión:**
  - **Un archivo por integrante** en [[tec/data-steward-agentico/tareas/_index|tareas/]] (`tareas/<rama>.md`), con una línea por tarea: ID, estado en la casilla, `vence`, `listo cuando` y, opcionales, `apoyo`, `depende`, `bloqueo` y `nota`.
  - **Un responsable por tarea:** la tarea vive solo en el archivo de su responsable; el apoyo solo se menciona.
  - **Estados:** `[ ]` pendiente, `[/]` en proceso, `[x]` listo y `[!]` bloqueado con motivo.
  - **Publicación sin PR:** cada 15 minutos, `sincronizar.yml` copia a `main` el archivo de tareas de cada rama si es válido y si la rama ya tiene la última versión de `main` de ese archivo. Si no es válido, abre un issue a esa persona.
  - **Tablero generado:** [[tec/data-steward-agentico/tareas/_tablero|_tablero.md]] con hitos, bloqueadas, vencidas, lo que vence hoy y mañana, lo que se destrabó y el avance por frente y por persona. Nadie lo edita.
  - **Novedades sin ruido:** los cambios de `tareas/` no aparecen en `novedades.md`; su estado está en el tablero.
  - **Carga semanal:** juan-pablo carga las tareas de cada semana el lunes, en un solo PR. El Excel queda como referencia del plan completo; la semana en curso vive en el vault.
- **Por qué:** cada quien solo toca su archivo, así que no hay conflictos y cabe en la validación de áreas sin excepciones. Marcar una tarea no cuesta un PR. Claude, ChatGPT y Gemini ven el estado real del equipo en el vault.
- **Alternativas descartadas:**
  - Una sola página de tareas compartida: conflictos constantes al propagar y choca con la validación de áreas.
  - Auto-merge de PRs que solo tocan tareas: con una rama por persona, el PR casi siempre lleva otros cambios, así que casi nunca aplicaría.
  - GitHub Projects: tiene tablero, pero los asistentes de IA del equipo no lo leen.
  - Seguir solo con el Excel: nadie lo ve a diario y se desactualiza.
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]], [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|vault compartido del equipo]]
