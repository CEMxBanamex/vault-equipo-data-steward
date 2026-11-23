---
tipo: sesion
fecha: 2026-11-23
autor: juan-pablo
resumen: Plan y tareas de la semana 3, revisión de los PR abiertos, S1-06 cerrada, Ollama de Carlos Ramos conectado a dev, MCP como dev-ana y endpoint de URL prefirmada para subir a S3 (S3-04) probado en dev.
---
# Sesión 2026-11-23: semana 3, revisión de PR y subida a S3

Trabajo con Claude Code en el repo de código y en el vault. Sigue a [[tec/data-steward-agentico/sesiones/2026-11-22-juan-pablo-despliegue-dev|despliegue de dev]].

## Qué se hizo

### Plan y tareas
| Paso | Resultado |
|---|---|
| Diagnóstico | Al empezar, 4 tareas mías vencidas (S1-06, S1-08, S1-09 y S1-11) y varios pendientes de infraestructura sin tarea |
| Plan de la semana 3 | [[tec/data-steward-agentico/plan-de-trabajo/plan-semana-3-demo\|Plan de la semana 3]]: corte el martes a las 17:00, ensayo a las 20:00, demo el miércoles 25 y MVP el domingo 29 |
| Tareas S3-01 a S3-38 | Cargadas en los archivos de `tareas/` (PR 16, 17 y 18 del vault) |
| Ajustes al borrador | S1-08 pasa al 27; S1-11 cerrada; S3-11 y S3-15 ya no esperan a S3-12; S3-08 (prod) después de S3-09 (JWT); S3-37 nueva (contexto del usuario en el MCP) |
| S1-06 cerrada | Los contratos de tools (`datos/steward_datos/contratos.py`) y del chat (`contratos/eventos_sse.py`) quedan congelados en dev. Carlos Ramos reportó que S1-06 lo bloqueaba |
| S3-38 nueva | Vía rápida para facturas en XML (CFDI 4.0), para Carlos Delgado el jueves 26 |

### Revisión de PR del repo de código
| PR | Autor | Resultado |
|---|---|---|
| 21 (S1-40) | Mauricio | Aprobado, actualizado con dev y fusionado; desplegado en dev |
| 19 (tools de Datos en el MCP) | Carlos Delgado | Cambios pedidos: falta `usuario_actual.set(usuario)`; sin eso `obtener_metrica` falla por MCP (S3-37) |
| 13 (stubs, bitácora, redactor, MSW) | Yael | Cambios pedidos: lint en rojo, `consultar_bitacora` sin permisos por usuario y cita inventada `P-XXX` en el redactor |
| 18 (endpoints del chat) | Mauricio | Comentario: usar `PasoEvent` y `RespuestaEvent` del contrato (S3-01) |
| 20 (chat con MSW) | Mauricio | Comentario: agregar `tipo` y `fuentes` a la respuesta y resolver el choque con el 13 |
| 30 (S3-11, grafo de casos real) | Carlos Delgado | Revisado, sin publicar. Buen código; choca con la demo: la confianza siempre es nula (el escenario de baja confianza no funciona) y solo lee PNG y JPEG |

### Infraestructura de dev
| Paso | Resultado |
|---|---|
| Ollama en dev (S3-02) | La laptop de Carlos Ramos responde desde `dsa-dev` por Tailscale. `/dsa/dev/ollama_base_url` apunta a ella (el valor está en SSM, no aquí) |
| Modelos de esa laptop | Tenía `qwen2.5-coder:7b` y `llama3.2:1b`; faltan `gemma3:4b` y `embeddinggemma:300m` (los está bajando) |
| Usuario del MCP en dev | `/dsa/dev/mcp_dev_usuario = dev-ana`, creado a mano con la CLI (fuera de Terraform). No hizo falta cambiar código: el contenedor `mcp` usa `env_file: .env` |
| Reinicio | `systemctl restart dsa-arranque` regeneró el `.env`; `mcp` y `backend` sanos y `/api/health` en 200 |
| Base `dsa_dev` | Migración 0003, 27 tablas, sin datos. Lista para la primera carga (S3-03) |
| CORS del bucket de dev | Permite `PUT` y `GET` desde `https://dev.cem-steward.online` |
| S3-04 | Endpoint `POST /api/casos/url-subida` (PR 31 del repo de código), fusionado y desplegado. Detalle abajo |

### S3-04: subida directa a S3
- **Qué hace:** el backend firma una URL temporal (15 minutos) para que el navegador suba un archivo directo al bucket privado, sin credenciales en el navegador. Ver [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3|la decisión]].
- **Contrato:** el que ya usaba el frontend del PR 13. Entrada `nombre_archivo` y `tipo_documento`; salida `upload_url`, `s3_key` (`casos/<uuid>/<archivo>`), `expira_en_segundos` y `content_type` (nuevo).
- **Validaciones:** extensión según el tipo de caso (facturas en PDF, PNG o JPG; validación con políticas en CSV, Excel o PDF) y nombre saneado. El `Content-Type` va dentro de la firma.
- **Credenciales:** en dev firma con el perfil de la EC2 (IMDSv2 con salto 2). En local, con el S3 de SeaweedFS y `S3_ENDPOINT_PUBLICO`.
- **Prueba en dev** (desde la EC2 por SSM Run Command):

| Prueba | Resultado |
|---|---|
| Pedir la URL | 200, firmada para el bucket de dev, 900 s |
| Preflight CORS con origen `dev.cem-steward.online` | 200, permite `GET, PUT` |
| `PUT` del archivo | 200; en el bucket con cifrado AES256 |
| `PUT` con otro `Content-Type` | 403 |
| Archivo `.exe` | 422 |
| Limpieza | Archivo de prueba borrado; bucket vacío |

## Decisiones
- **S1-06 sin junta:** los contratos vigentes son los que ya están en dev; los endpoints del chat (PR 18) y `consultar_bitacora` (PR 13) se ajustan en sus PR dentro de S3-01.
- **El sistema recibe PDF.** S3-04 acepta PDF para facturas; falta que el grafo de casos (PR 30) convierta la primera página a imagen antes de mandarla a `gemma3:4b`. Propuesta: `pypdfium2` (licencia Apache/BSD, sin programas del sistema).
- **Facturas en XML (CFDI) después de la demo:** en México la factura legal es el XML; si llega, se lee con código y sin modelo (S3-38). Verificar el sello y el estatus en el SAT queda como trabajo futuro.
- **Modelo del chat para la demo:** lo decide Carlos Ramos (S3-15). Recomendación: medir con `ollama ps`; si `qwen2.5-coder:7b`, `gemma3:4b` y `embeddinggemma:300m` no caben juntos en 8 GB de VRAM, usar `gemma3:4b` también en el chat y dejar Qwen para el SQL del analista de datos.
- **No se instala Tailscale en un equipo ni en una red de trabajo.** La EC2 ya está en la tailnet y las pruebas se hacen desde ella por SSM.

## Problemas y cómo se resolvieron
| Problema | Causa | Solución |
|---|---|---|
| El hook local de Git Guardian bloqueó un commit | Marca `.env.example` como archivo de entorno (falso positivo) | Se quitó ese cambio del commit; el valor por omisión quedó en `docker-compose.dev.yml`. No se saltó el hook |
| La API de dev responde "Connection reset by peer" desde la red del trabajo de Juan Pablo | El firewall de esa red empezó a bloquear el dominio | Probar desde la EC2 por SSM; ensayo y demo desde una red personal |
| `aws` fallaba con las opciones en una variable | zsh no separa variables en palabras | Escribir las opciones directo en el comando |

## Pendientes
- **S3-02:** que la laptop de Carlos Ramos termine de bajar `gemma3:4b` y `embeddinggemma:300m`, y revisar con `/api/ps` desde `dsa-dev` qué queda cargado.
- **S3-03:** correr la carga en la EC2 (`docker compose --profile tareas run --rm carga`) en cuanto esté `embeddinggemma:300m`. Solo se puede correr una vez sobre una base vacía.
- **PR 30:** publicar la revisión o comentarla con Carlos Delgado; soporte de PDF y el escenario de baja confianza (cambiarlo por uno de la lista 69-B, R-019 del PR 29, es lo más seguro).
- **PR 13, 18, 19 y 20:** nadie ha subido cambios desde las revisiones.
- **Integración de mañana (S3-30):** el grafo del PR 30 guarda el estado en memoria y recibe una ruta local; la API necesita una instancia global para `dev-ana`, descargar el archivo de S3 a un temporal y no reiniciar el backend entre la subida y la decisión.
- `mcp_dev_usuario` está fuera de Terraform: si se recrea `envs/dev`, hay que volver a crearlo.

## Siguiente paso
Cargar los datos en `dsa_dev` en cuanto Carlos Ramos tenga los modelos, y destrabar los PR 19, 18 y 13 para que S3-11, S3-30 y S3-31 lleguen al corte del martes a las 17:00.
