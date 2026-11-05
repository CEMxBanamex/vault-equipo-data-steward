---
tipo: area
fecha: 2026-10-28
resumen: Diseño de las interfaces del MVP: las seis pantallas del mockup, sus estados, el sistema de diseño y los supuestos tomados.
---
# interfaces

## Qué cubre
Mockup de alta fidelidad hecho a partir del brief de diseño del socio formador. Base de escritorio 1440 × 900, funciona hasta 1024 px. Flujo navegable: inicio de sesión → bandeja → subir caso → detalle del caso.

- **Mockup (lienzo de diseño en Claude, privado):** https://claude.ai/code/artifact/cdba0732-5e2f-4e5c-b067-50c7bff5287c
- **Imágenes PNG:** fuera del vault (zip `data_steward_pantallas.zip`), porque llevan el logo del socio formador.

## Estructura común
- **Barra superior:** logo, nombre del producto ("Data Steward"), usuario con su rol y "Cerrar sesión".
- **Menú lateral:** Casos · Subir caso · Bitácora · Políticas (solo administrador).
- El rol define qué opciones del menú se ven.

## Pantallas
| # | Pantalla | Prioridad | Usuario | Nota |
|---|---|---|---|---|
| 1 | Inicio de sesión | MVP | Todos | [[tec/data-steward-agentico/interfaces/pantalla-inicio-de-sesion\|inicio de sesión]] |
| 2 | Bandeja de casos | MVP | Todos | [[tec/data-steward-agentico/interfaces/pantalla-bandeja-de-casos\|bandeja de casos]] |
| 3 | Subir caso | MVP | Analistas | [[tec/data-steward-agentico/interfaces/pantalla-subir-caso\|subir caso]] |
| 4 | Detalle de factura | MVP | Analista de cuentas por pagar | [[tec/data-steward-agentico/interfaces/pantalla-detalle-factura\|detalle de factura]] |
| 5 | Detalle de validación con políticas | Prioridad 2 | Analista de datos | [[tec/data-steward-agentico/interfaces/pantalla-detalle-validacion\|detalle de validación]] |
| 6 | Bitácora | Prioridad 2 | Todos | [[tec/data-steward-agentico/interfaces/pantalla-bitacora\|bitácora]] |
| 7 | Políticas | Opcional | Administrador | Sin diseñar |
| 8 | Estado del sistema | Opcional | Demo | Sin diseñar |

## Notas
- [[tec/data-steward-agentico/interfaces/sistema-de-diseno|Sistema de diseño]]: paleta, tipografía y componentes para React.
- [[tec/data-steward-agentico/interfaces/decision-supuestos-del-mockup|Decisión: supuestos del mockup]]

## Reglas que aplican a todas las pantallas
- Ningún botón para pagar, liberar o autorizar (coincide con [[tec/data-steward-agentico/agentes/decision-sin-tool-para-liberar-pagos|ninguna tool para liberar pagos]]).
- Se dice "resultado sugerido", nunca "aprobado".
- Todo estado lleva color **y** ícono o texto.
- Datos de ejemplo siempre ficticios.

## Pendientes
- Validar con el equipo el resultado sugerido del caso V-0207 (se puso "Rechazado").
- Conseguir el logotipo completo del socio formador (solo se recibió el símbolo).
- Diseñar las pantallas 7 y 8 si da tiempo.
- Repartir las pantallas entre el equipo para el frontend.


## Actualización 2026-10-28 (chat)
- **Cambio de alcance:** se quita la LSTM y el socio formador pide un chat de facturas con los pasos del agente visibles. Ver [[tec/data-steward-agentico/chat/_index|chat]].
- **Pantallas nuevas o modificadas:**
  - **Asistente:** pantalla nueva del chat global, en el menú lateral junto a Casos, Subir caso y Bitácora.
  - **Detalle de factura y detalle de validación:** panel o pestaña "Preguntar sobre este caso".
  - Preguntas sugeridas al iniciar, como "¿Por qué este resultado?" o "¿Qué regla falló?".
- **Componente de pasos:** línea que cambia, se expande en lista y queda como resumen "✓ 4 pasos · 3.2 s ›". Ver [[tec/data-steward-agentico/chat/decision-pasos-del-agente-visibles|decisión]].
- **Pendiente:** agregar el panel de chat y la pantalla Asistente al mockup.
- Responsables del frontend: Yael García y Mauricio Guerrero.

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/interfaces/decision-supuestos-del-mockup\|decision-supuestos-del-mockup]] | decision |  | 2026-10-28 | Qué se decidió o inventó en el mockup porque el brief no lo definía, y qué queda por validar. |
| [[tec/data-steward-agentico/interfaces/pantalla-bandeja-de-casos\|pantalla-bandeja-de-casos]] | pantalla |  | 2026-10-28 | Pantalla 2, lista de casos con resumen, filtros y tabla; desde aquí se abre el detalle de cada caso. |
| [[tec/data-steward-agentico/interfaces/pantalla-bitacora\|pantalla-bitacora]] | pantalla |  | 2026-10-28 | Pantalla 6, registro de solo lectura de todo lo que hacen las personas y el agente, con filtros, exportación y filas expandibles. |
| [[tec/data-steward-agentico/interfaces/pantalla-detalle-factura\|pantalla-detalle-factura]] | pantalla |  | 2026-10-28 | Pantalla 4, la más importante: documento original a la izquierda; datos extraídos, hallazgos y resultado sugerido a la derecha; la persona confirma, corrige o escala. |
| [[tec/data-steward-agentico/interfaces/pantalla-detalle-validacion\|pantalla-detalle-validacion]] | pantalla |  | 2026-10-28 | Pantalla 5, como el detalle de factura pero con los registros en tabla, filas con problema resaltadas y la lista de políticas consultadas. |
| [[tec/data-steward-agentico/interfaces/pantalla-inicio-de-sesion\|pantalla-inicio-de-sesion]] | pantalla |  | 2026-10-28 | Pantalla 1, entrada a la app con un solo botón; el acceso lo resuelve el proveedor externo (Cognito). |
| [[tec/data-steward-agentico/interfaces/pantalla-subir-caso\|pantalla-subir-caso]] | pantalla |  | 2026-10-28 | Pantalla 3, alta de un caso en dos pasos (tipo de revisión y archivos) con sus errores de carga. |
| [[tec/data-steward-agentico/interfaces/sistema-de-diseno\|sistema-de-diseno]] | referencia |  | 2026-10-28 | Paleta en hex, tipografía, componentes reutilizables para React y reglas de accesibilidad del mockup. |
<!-- indice-automatico:fin -->
