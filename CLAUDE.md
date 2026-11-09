# CLAUDE.md

# Vault del equipo: Data Steward Agéntico

Este repo es la memoria compartida del proyecto para el Equipo 1. Lo usamos las personas en Obsidian y también Claude (Claude Desktop o Claude Code con el MCP de Obsidian). Son archivos Markdown enlazados con [[wikilinks]].

El proyecto vive en `tec/data-steward-agentico/`. Empieza por su `CLAUDE.md`.

## Al empezar
Lee `tec/data-steward-agentico/novedades.md`: lista los últimos 20 cambios que llegaron a `main`, con liga a cada nota. Si una novedad toca lo que te piden, abre la nota enlazada antes de responder. Ese archivo lo genera GitHub Actions; nadie lo edita.

## Antes de escribir (para Claude)
- Pregunta quién es la persona con la que trabajas si no lo sabes: su nombre de rama (`juan-pablo`, `iris`, `mario`, `carlos-delgado`, `carlos-ramos`, `yael`, `mauricio`) va en el campo `autor` y decide qué áreas puede editar.
- Revisa la tabla de dueños. Si te piden cambiar una nota de un área que no es de esa persona, no la edites: crea una propuesta (ver abajo).
- Dile qué notas cargaste antes de empezar.

## Dueños por área
Solo los dueños editan notas existentes de su área. **juan-pablo puede modificar todo el vault**, incluidas las áreas y sesiones de los demás, como responsable de la organización del proyecto.

| Área | Dueños |
|---|---|
| `arquitectura/`, `plan-de-trabajo/`, `producto/`, `CLAUDE.md`, workflows y scripts | juan-pablo |
| `tools/` | Cada nota de tool, su responsable (ver el índice de `tools/`); el `_index.md` y las notas nuevas, juan-pablo |
| `agentes/`, `modelos/`, `chat/` | carlos-delgado, carlos-ramos; cada dueño de agente también edita la nota de su agente |
| `interfaces/` | yael, mauricio |
| `sesiones/` | Cada quien las suyas |

La fuente de verdad de los dueños es `.github/CODEOWNERS`.

**Esto lo revisa el check "Validar vault" en cada PR.** Si modificas, borras o renombras un archivo que no es de tu área, el PR no se puede fusionar. Fuera de tus áreas solo puedes crear o editar:
- Tus propuestas: `<carpeta>/propuesta-<tema>-<tu-rama>.md`.
- Tus sesiones: `sesiones/AAAA-MM-DD-<tu-rama>-<tema>.md`.

## Reglas para no tener conflictos en Git
1. **Notas nuevas en lugar de editar notas ajenas.** Para cambiar algo de otra área, crea `<area>/propuesta-<tema>-<tu-rama>.md` con la plantilla `_equipo/plantillas/propuesta.md`. El dueño la integra.
2. **Sesiones con autor en el nombre:** `sesiones/AAAA-MM-DD-<tu-rama>-<tema>.md`. Así dos sesiones del mismo día nunca chocan.
3. **No edites `novedades.md` ni la sección automática de los `_index.md`** (entre `<!-- indice-automatico:inicio -->` y `<!-- indice-automatico:fin -->`). La regenera GitHub Actions. El resto del índice lo edita su dueño.
4. **Nunca borres ni sobrescribas notas.** Para corregir algo, el dueño agrega una sección nueva con fecha al final.
5. **Frontmatter obligatorio** en toda nota nueva: `tipo`, `fecha` (AAAA-MM-DD), `autor` (tu rama) y `resumen` (una línea). Usa las plantillas de `_equipo/plantillas/`.
6. **Enlaces con ruta completa desde la raíz:** `[[tec/data-steward-agentico/tools/_index|tools]]`. En una tabla, escapa la barra: `\|`.

## Flujo de Git
- Cada quien trabaja **solo en su rama**. Nunca se sube directo a `main`.
- Para llevar cambios a `main`, abre un Pull Request. Se valida solo (frontmatter, enlaces, sección automática y secretos) y GitHub pide revisión a los dueños del área tocada.
- Al fusionar a `main`, GitHub Actions regenera los índices y propaga `main` a todas las ramas.
- Haz pull de tu rama antes de empezar a trabajar (Obsidian Git lo hace al abrir).
- Si el Action no puede propagar `main` a tu rama por un conflicto, te abre un issue con los archivos y cómo resolverlo.

## Qué NO va en el vault
- Credenciales, tokens, llaves, cadenas de conexión ni IDs sensibles. El PR se bloquea si se detectan.
- Datos reales del socio formador. Solo datos sintéticos o autorizados.
- Código completo: vive en el repo de código. Aquí solo se describe la lógica y se enlaza.

## Si falla la conexión
Si Claude no puede leer o escribir en el vault, debe decirlo. No inventa contexto ni responde como si hubiera leído notas que no abrió.
