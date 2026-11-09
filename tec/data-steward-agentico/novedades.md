---
tipo: novedades
fecha: 2026-11-09
autor: vault-bot
resumen: Los últimos 20 cambios que llegaron a main, con liga a cada nota. Léelo al empezar.
---
# Novedades del vault

_Lo genera GitHub Actions en cada cambio a `main`. No lo edites a mano._

Muestra los últimos 20 cambios, del más reciente al más antiguo. Si una novedad toca lo que te piden, abre la nota enlazada antes de responder. Para cambios más antiguos, consulta el historial de Git de `main`.

## 2026-11-09

### ci: generar novedades.md en cada cambio a main · juan-pablo · PR #4
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Modificada:** [[tec/data-steward-agentico/CLAUDE|CLAUDE]]
  MVP de Data Steward Agéntico para un reto del Tec con un banco como socio formador: agentes LangGraph con tools por MCP que revisan facturas y registros contra políticas, explican cada recomendación y dejan la decisión a una persona.
- **Cambios en el repo:** `.github/workflows/sincronizar.yml`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md` y 1 más

### Juan pablo · juan-pablo · PR #3
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Cambios en el repo:** `AGENTS.md`, `GEMINI.md`, `README.md`

## 2026-11-04

### docs: sesión de implementación del repo del equipo · juan-pablo · PR #1
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-04-juan-pablo-implementacion-repo-equipo|2026-11-04-juan-pablo-implementacion-repo-equipo]]
  Implementación del repo compartido del vault: estructura, ramas, token, sincronización, validación de áreas, protección de main y repo público.

### ci: validar que cada integrante solo modifique sus áreas · Juan Pablo Perez · push directo
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Cambios en el repo:** `.github/CODEOWNERS`, `.github/integrantes.txt`, `.github/workflows/validar-vault.yml`, `CLAUDE.md`, `scripts/validar_vault.py`

### Full Context and Organization / Juan Pablo · Juan Pablo Perez · push directo
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|decision-checkpoints-y-bitacora-separados]]
  Los checkpoints de LangGraph son el estado operativo del caso; la bitácora de auditoría es una tabla propia y es el registro oficial.
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-sin-tool-para-liberar-pagos|decision-sin-tool-para-liberar-pagos]]
  El servidor MCP no expone ninguna tool para liberar pagos ni ejecutar operaciones, así que el límite del agente lo impone la arquitectura y no solo el prompt.
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|decision-validaciones-deterministas-en-codigo]]
  Sumas, campos obligatorios y formatos se comprueban con código determinista en la tool validar_reglas; el LLM extrae, busca y explica, pero no calcula.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|decision-jwt-al-final]]
  El login con Cognito por correo se conecta temprano en el frontend, pero la validación del JWT en las APIs se activa al final con un interruptor AUTH_MODE, para probar fácil con Postman.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-monolito-modular|decision-monolito-modular]]
  Un solo repositorio y un solo servicio desplegable, con los agentes como nodos de un grafo LangGraph, porque es lo más simple de desplegar y depurar para un MVP con equipo chico.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3|decision-subida-directa-a-s3]]
  El navegador sube el archivo del caso directo a S3 con una URL prefirmada, sin pasar por el backend.
- **59 notas más** en `agentes/`, `arquitectura/`, `chat/`, `interfaces/`, `modelos/`, `plan-de-trabajo/`, `producto/`, `sesiones/`, `tec/data-steward-agentico/`, `tools/`
- **Cambios en el repo:** `.gitattributes`, `.github/CODEOWNERS`, `.github/integrantes.txt`, `.github/workflows/sincronizar.yml`, `.github/workflows/validar-vault.yml` y 13 más
