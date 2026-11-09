# GEMINI.md

Instrucciones para asistentes de IA (ChatGPT, Codex, Gemini, Antigravity u otros) que trabajen en este repo. Son las mismas reglas que sigue Claude; la versión completa está en `CLAUDE.md`. **Léelo antes de escribir cualquier nota.**

## Qué es este repo
Vault de Obsidian del Equipo 1 para el reto Data Steward Agéntico. Son notas Markdown enlazadas con [[wikilinks]]. El proyecto vive en `tec/data-steward-agentico/`; empieza por su `CLAUDE.md` y por el `_index.md` de cada área.

## Antes de escribir
1. Pregunta con quién trabajas si no lo sabes. Su nombre de rama (`juan-pablo`, `iris`, `mario`, `carlos-delgado`, `carlos-ramos`, `yael`, `mauricio`) va en el campo `autor` y decide qué puede editar.
2. Revisa en `.github/CODEOWNERS` de quién es cada archivo. Solo edita archivos del área de esa persona.
3. Para cambiar algo de otra área, no lo edites: crea `<carpeta>/propuesta-<tema>-<rama>.md` con la plantilla `_equipo/plantillas/propuesta.md`.

## Reglas
- Sesiones nuevas en `tec/data-steward-agentico/sesiones/AAAA-MM-DD-<rama>-<tema>.md`.
- Toda nota nueva lleva frontmatter con `tipo`, `fecha` (AAAA-MM-DD), `autor` (rama) y `resumen` (una línea). Usa las plantillas de `_equipo/plantillas/`.
- Enlaces con ruta completa desde la raíz: `[[tec/data-steward-agentico/tools/_index|tools]]`. En tablas, escapa la barra: `\|`.
- No edites la sección entre `<!-- indice-automatico:inicio -->` y `<!-- indice-automatico:fin -->` de los `_index.md`.
- Nunca borres ni sobrescribas notas. Las correcciones las hace el dueño con una sección nueva con fecha al final.
- No toques `.github/`, `scripts/`, `CLAUDE.md`, `AGENTS.md` ni `GEMINI.md`.
- Nada de credenciales, tokens ni datos reales del socio formador. El repo es público.
- No inventes contexto: si no leíste una nota, no respondas como si la conocieras.

## Git
- Se trabaja solo en la rama de la persona, nunca en `main`.
- Los cambios llegan a `main` por Pull Request; el check "Validar vault" revisa frontmatter, enlaces, índices, áreas y secretos.
