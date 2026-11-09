# Vault del equipo: Data Steward Agéntico

Memoria compartida del proyecto en Obsidian: decisiones, arquitectura, agentes, tools, interfaces, plan de trabajo y sesiones. Las reglas completas están en [`CLAUDE.md`](CLAUDE.md).

## Primera vez

1. **Clona el repo y cambia a tu rama:**
   ```bash
   git clone <URL-del-repo>
   cd <carpeta-del-repo>
   git checkout <tu-rama>
   ```
   Ramas: `juan-pablo`, `iris`, `mario`, `carlos-delgado`, `carlos-ramos`, `yael`, `mauricio`.

2. **Abre la carpeta del repo como vault** en Obsidian ("Abrir carpeta como vault").

3. **Configura los enlaces** en *Ajustes → Archivos y enlaces*:
   - *Formato de enlace nuevo:* **Ruta absoluta en el vault**.
   - *Usar [[Wikilinks]]:* activado.

   Así los enlaces que crees siguen la misma convención que el resto del vault.

4. **Instala el plugin Obsidian Git** (*Ajustes → Plugins de la comunidad*) y configúralo:
   - *Pull on startup:* activado.
   - *Auto commit-and-sync interval:* 10 minutos (o el que prefieras).
   - Verifica que esté en tu rama, no en `main`.

5. **Opcional, para usar Claude:** instala el plugin *Local REST API* y conecta el MCP de Obsidian en Claude Desktop. Claude leerá el `CLAUDE.md` y seguirá las mismas reglas.

## Día a día

1. Abre Obsidian (hace pull de tu rama).
2. Trabaja en tus áreas. Para notas nuevas, usa las plantillas de `_equipo/plantillas/`.
3. Obsidian Git sube tus cambios a tu rama.
4. Cuando algo esté listo para el equipo, abre un **Pull Request de tu rama a `main`** en GitHub.
5. Al fusionarse, todos reciben el cambio en su rama en unos minutos.

## Reglas rápidas

- Edita solo notas de tus áreas. Para proponer cambios en otra área, crea una nota `propuesta-<tema>-<tu-rama>.md`.
- Tus sesiones van en `sesiones/AAAA-MM-DD-<tu-rama>-<tema>.md`.
- No edites la sección "Índice automático" de los `_index.md`.
- Nada de credenciales ni datos reales.

## Si GitHub te abre un issue de conflicto

Pasó porque tu rama y `main` cambiaron lo mismo. En tu rama:

```bash
git pull origin main
# resuelve los archivos marcados en conflicto
git add .
git commit -m "fix: resolver conflicto con main"
git push
```

Luego cierra el issue.

## Automatizaciones

| Workflow | Cuándo corre | Qué hace |
|---|---|---|
| `validar-vault.yml` | En cada Pull Request a `main` | Revisa frontmatter, enlaces, la sección automática de los índices y busca secretos |
| `sincronizar.yml` | En cada cambio a `main`, a diario a medianoche y a mano | Regenera los índices y propaga `main` a la rama de cada integrante |

## Usar ChatGPT o Gemini con el vault

El MCP de Obsidian solo funciona con Claude Desktop, porque es local. ChatGPT y Gemini en la web solo se conectan a servidores MCP remotos, así que no pueden usarlo. Tienes dos opciones:

**1. Un agente de terminal dentro del repo (recomendado).** Abre la terminal en la carpeta del repo, en tu rama, y usa la CLI de tu asistente (por ejemplo Gemini CLI, Antigravity CLI o la CLI de OpenAI). Lee las notas como archivos y sigue las reglas de `AGENTS.md` o `GEMINI.md`. Revisa con `git status` lo que cambió antes de hacer commit.

**2. ChatGPT o Gemini en la web.** Pega el enlace de la nota en GitHub o súbela como archivo. Empieza la conversación con:

> Trabajo en el vault del equipo Data Steward Agéntico. Mi rama es `<tu-rama>`. Sigue las reglas de AGENTS.md: solo propongo cambios en mis áreas, las notas nuevas llevan frontmatter con tipo, fecha, autor y resumen, y los enlaces usan la ruta completa desde la raíz.

Después copia el resultado a la nota en Obsidian.
