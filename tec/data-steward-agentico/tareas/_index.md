---
tipo: area
fecha: 2026-11-09
autor: juan-pablo
resumen: Tareas por integrante con su estado (un archivo por persona) y el tablero que las junta; cómo marcar una tarea y el formato de cada línea.
---
# tareas

## Qué cubre
Lo que tiene que hacer cada integrante, semana por semana, y si ya está listo. Cada persona tiene su archivo y solo ella lo marca. El estado del equipo se ve en [[tec/data-steward-agentico/tareas/_tablero|el tablero]], que se genera solo. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-tareas-por-integrante|la decisión]].

## Archivos
| Archivo | Quién lo edita |
|---|---|
| [[tec/data-steward-agentico/tareas/juan-pablo\|juan-pablo]] | Juan Pablo |
| [[tec/data-steward-agentico/tareas/iris\|iris]] | Iris |
| [[tec/data-steward-agentico/tareas/mario\|mario]] | Mario |
| [[tec/data-steward-agentico/tareas/carlos-delgado\|carlos-delgado]] | Carlos Delgado |
| [[tec/data-steward-agentico/tareas/carlos-ramos\|carlos-ramos]] | Carlos Ramos |
| [[tec/data-steward-agentico/tareas/yael\|yael]] | Yael |
| [[tec/data-steward-agentico/tareas/mauricio\|mauricio]] | Mauricio |
| [[tec/data-steward-agentico/tareas/_tablero\|_tablero]] | Nadie: lo genera GitHub Actions |

## Cómo marcar una tarea
1. En tu rama, abre tu archivo de tareas y cambia la casilla. En Obsidian basta con hacer clic; para `[/]` y `[!]`, escribe el carácter entre los corchetes.
2. Guarda. Obsidian Git lo sube a tu rama (o haz commit y push).
3. **No hace falta Pull Request.** Cada 15 minutos, GitHub Actions copia tu archivo de tareas a `main`, actualiza el tablero y propaga `main` a todas las ramas.
4. Si tu archivo tiene un error de formato, no se publica y GitHub te abre un issue con la línea a corregir. Cuando lo corriges, se publica y el issue se cierra solo.

El resto de tus cambios (notas, sesiones, propuestas) sigue llegando a `main` por Pull Request, como siempre.

## Estados
| Casilla | Estado | Cuándo |
|---|---|---|
| `[ ]` | Pendiente | No has empezado |
| `[/]` | En proceso | Ya empezaste |
| `[x]` | Listo | Se cumple el "listo cuando" |
| `[!]` | Bloqueado | No puedes avanzar; agrega `· bloqueo: <motivo>` |

## Formato de una tarea
Una línea por tarea, con los campos separados por ` · `:

`- [ ] **S1-01** Título · vence: 2026-11-10 · apoyo: mario · depende: S1-07, S1-08 · listo cuando: <criterio que se puede comprobar> · nota: <opcional>`

- **ID:** `S<semana>-<nn>` para las tareas del plan (las asigna juan-pablo). Si agregas una tarea tuya, usa `<tu-rama>-<nn>` (por ejemplo, `iris-01`).
- **Obligatorios:** `vence` (AAAA-MM-DD) y `listo cuando`.
- **Opcionales:** `apoyo` (ramas separadas por comas, o `todos`), `depende` (IDs), `bloqueo` (obligatorio si está en `[!]`) y `nota`.
- **Hitos:** un `#hito` en el título la marca como hito del equipo.
- Cada tarea vive solo en el archivo de su responsable; el apoyo solo se menciona. Así nunca hay dos lugares que marcar.
- Las tareas de cada semana van bajo un encabezado `## Semana N · fechas`.

## Reglas
- Solo editas tu archivo. Para cambiar una tarea de otra persona (fecha, criterio, responsable), díselo o pídeselo a juan-pablo.
- juan-pablo carga las tareas de cada semana el lunes, en un solo PR. Si en ese momento también marcaste algo, puede haber un conflicto: el Action te abre un issue con cómo resolverlo.
- No edites `_tablero.md`: lo sobrescribe el Action.
- El check "Validar vault" también revisa el formato de las tareas cuando llegan por PR.

## Para los asistentes de IA
- Al empezar, lee el tablero y el archivo de tareas de la persona con la que trabajas.
- Cuando terminen algo que corresponde a una tarea, propón marcarla y, si aplica, actualizar la `nota`. Nunca edites el archivo de tareas de otra persona.
