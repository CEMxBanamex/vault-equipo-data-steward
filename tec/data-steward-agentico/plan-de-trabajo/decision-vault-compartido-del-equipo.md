---
tipo: decision
fecha: 2026-11-04
autor: juan-pablo
resumen: El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
---
# Decisión: vault compartido del equipo

- **Contexto:** el equipo necesita el contexto del proyecto y poder modificarlo, sin merge conflicts al subir cambios a GitHub.
- **Decisión:**
  - **Repo de la organización** con solo este proyecto, en la misma ruta que en el vault personal (`tec/data-steward-agentico/`) para que los enlaces no se rompan. Incluye `tec/_compartido/ollama-gpus-por-tailscale.md`, la única ficha externa enlazada.
  - **Ramas:** `main` más una por integrante (`juan-pablo`, `iris`, `mario`, `carlos-delgado`, `carlos-ramos`, `yael`, `mauricio`).
  - **Hacia `main`:** solo por Pull Request, validado por `validar-vault.yml` (frontmatter, enlaces, sección automática de índices y secretos con gitleaks). `CODEOWNERS` pide revisión a los dueños del área.
  - **Desde `main`:** `sincronizar.yml` corre en cada push a `main`, a diario a medianoche (respaldo) y a mano. Regenera los índices automáticos y propaga `main` a cada rama. Si hay conflicto, no fuerza nada: abre un issue a esa persona.
  - **Token:** el Action usa un token personal de Juan Pablo (`VAULT_BOT_TOKEN`) para poder escribir en `main` protegida y en las ramas.
- **Reglas anticonflicto:**
  - Dueños por área; solo ellos editan notas existentes de su área.
  - Fuera de tu área, notas nuevas `propuesta-<tema>-<rama>.md`.
  - Sesiones con autor en el nombre: `AAAA-MM-DD-<rama>-<tema>.md`.
  - Sección automática en los `_index.md` entre marcadores, que nadie edita a mano.
  - Campo `autor` obligatorio en notas nuevas.
  - Sin `registro.md` compartido: el historial de Git es el registro.
  - `.obsidian/` fuera de Git y saltos de línea LF para todos (`.gitattributes`).
- **Vault personal:** el repo del equipo es la fuente de verdad. En el vault personal, `tec/data-steward-agentico` será un enlace simbólico (o *junction* en Windows) a la carpeta del clon, y el Git personal ignora esa ruta.
- **Por qué:** las ramas solas no evitan conflictos; los evitan las reglas sobre qué archivos toca cada quien. Propagar en cada push mantiene las fusiones pequeñas.
- **Alternativas descartadas:** que el Action fusionara las ramas en `main` automáticamente (sin revisión); propagar solo una vez al día; copiar el proyecto entre ambos vaults a mano.
- **Archivos:** `vault-equipo-data-steward.zip` (CLAUDE.md y README del equipo, workflows, scripts, CODEOWNERS, integrantes y plantillas).
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]]


## Actualización 2026-11-04 (revisión automática de áreas)
- El check `Validar vault` ahora también revisa que cada integrante solo modifique, borre o renombre archivos de sus áreas, según `.github/CODEOWNERS` e `.github/integrantes.txt`.
- Fuera de sus áreas solo puede crear o editar sus propuestas (`propuesta-<tema>-<rama>.md`) y sus sesiones (`sesiones/AAAA-MM-DD-<rama>-<tema>.md`).
- La rama `juan-pablo` queda exenta: puede modificar todo.
- `CODEOWNERS` sigue avisando a los dueños, pero su aprobación no es obligatoria, para no crear cuellos de botella.
- Las notas nuevas de tools y el `_index.md` de `tools/` quedan a cargo de Juan Pablo; los dueños de agente también editan la nota de su agente.


## Actualización 2026-11-09 (otros asistentes de IA)
- Parte del equipo usa ChatGPT y Gemini. Sus apps web solo se conectan a servidores MCP remotos, así que no pueden usar el MCP de Obsidian, que es local.
- Se agregaron a la raíz del repo `AGENTS.md` y `GEMINI.md` con las reglas del vault, para los agentes de terminal que trabajen dentro del repo.
- El `README.md` del repo tiene una sección para usar ChatGPT o Gemini, en terminal o en la web, con un prompt de inicio.
