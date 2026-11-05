---
tipo: sesion
fecha: 2026-11-04
autor: juan-pablo
resumen: Implementación del repo compartido del vault: estructura, ramas, token, sincronización, validación de áreas, protección de main y repo público.
---
# Sesión 2026-11-04: implementación del repo del equipo

## Qué se hizo
- **Repo creado:** `CEMxBanamex/vault-equipo-data-steward`, clonado en la computadora de Juan Pablo fuera del vault personal y de OneDrive.
- **Estructura subida a `main`:** `CLAUDE.md` y `README.md` del equipo, workflows, scripts, `CODEOWNERS`, `integrantes.txt`, plantillas en `_equipo/plantillas/`, el proyecto en `tec/data-steward-agentico/` y la ficha `tec/_compartido/ollama-gpus-por-tailscale.md`.
- **Vault personal conectado:** `tec/data-steward-agentico` del vault personal es un junction a la carpeta del repo. El Git del vault personal ignora esa ruta y la carpeta original quedó respaldada fuera del vault.
- **Ramas creadas:** `juan-pablo`, `iris`, `mario`, `carlos-delgado`, `carlos-ramos`, `yael`, `mauricio`, con sus usuarios de GitHub en `integrantes.txt`.
- **Token y secreto:** token fine-grained de Juan Pablo con permisos de contenido, issues y workflows, guardado como `VAULT_BOT_TOKEN`.
- **Sincronización probada:** el workflow regeneró los índices automáticos y propagó `main` a las 7 ramas.
- **Revisión de áreas:** el check `Validar vault` ahora bloquea PR que modifiquen, borren o renombren archivos fuera del área de quien lo abre, usando `CODEOWNERS`. Fuera de su área cada quien solo puede crear sus propuestas y sus sesiones. La rama `juan-pablo` puede modificar todo.
- **`CODEOWNERS` actualizado:** Juan Pablo en todas las reglas, cada nota de tool con su responsable y cada nota de agente con su dueño.
- **Protección de `main`:** PR obligatorio, sin aprobaciones obligatorias, status checks activados y bypass permitido para administradores (lo necesita el bot).
- **Repo público:** en un repo privado de una organización gratuita la protección no se aplicaba. Al hacerlo público se aplica, y `CODEOWNERS` pide revisión automática.

## Aprendizajes
- Las ramas por integrante no evitan conflictos por sí solas; los evitan las reglas sobre qué archivos toca cada quien.
- Trabajar directo en `main` provoca rechazos de push, porque el bot sube commits de índices; hay que trabajar en la rama propia.
- Con el vault ligado al repo, Obsidian muestra el contenido de la rama en la que está el clon.
- La protección de ramas y `CODEOWNERS` no se aplican en repos privados de organizaciones con plan gratuito.

## Decisiones
- [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|Vault compartido del equipo]]
- [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|Reparto de tools y subequipos de agentes]]

## Pendientes
- Confirmar con el profesor que el contenido del reto se puede tener en un repo público; si no, regresarlo a privado y usar un workflow de vigilancia.
- Revisar el historial completo con gitleaks, porque los primeros commits no pasaron por el check.
- Terminar este PR de prueba y agregar `validar` como check obligatorio en la regla de `main`.
- Paso 7: incorporar al equipo (clonar, cambiar a su rama, configurar Obsidian y Obsidian Git).
- Actualizar el Excel con nombres individuales y dividir las subtareas de frontend entre Yael y Mauricio.

## Siguiente paso
Fusionar este PR, hacer obligatorio el check `validar` e incorporar al equipo.
