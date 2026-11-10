---
tipo: decision
fecha: 2026-11-10
autor: carlos-delgado
resumen: Inventario de las cinco GPUs del equipo y propuesta inicial de reparto para visión, chat, embeddings y respaldo.
---

# Inventario de GPUs y propuesta de reparto de modelos

## Objetivo y alcance

Registrar la GPU, la VRAM dedicada y la RAM de las cinco laptops disponibles y proponer su función en el prototipo. Este reporte cubre el inventario y el reparto propuesto solicitado en S1-25; no acredita el despliegue ni el rendimiento de los modelos en todas las máquinas.

## Inventario

| Responsable | GPU | VRAM dedicada | RAM del sistema |
| --- | --- | --- | --- |
| Carlos Delgado | NVIDIA GeForce RTX 4060 Laptop | 8 GB | 16 GB |
| Carlos Ramos | NVIDIA GeForce RTX 3070 | 8 GB | 40 GB |
| Mario | NVIDIA GeForce GTX 1650 | 4 GB | 16 GB |
| Juan Pablo | NVIDIA GeForce RTX 3050 | 4 GB | 16 GB |
| Yael | NVIDIA GeForce RTX 3050 | 4 GB | 16 GB |

**Fuente:** especificaciones comunicadas por Carlos Delgado el 10 de noviembre de 2026 a partir de la información de los integrantes. Para su equipo también compartió una captura de Información del sistema y confirmó la VRAM. No se inspeccionaron directamente las otras cuatro laptops.

Se confirman cinco equipos, contando por separado las laptops de Juan Pablo y Yael; esto actualiza el conteo preliminar de cuatro mencionado durante el levantamiento.

**Información complementaria disponible:**
- Carlos Delgado: Lenovo LOQ 16IRH8 (82XW), Intel Core i7-13620H.
- Carlos Ramos: Intel Core i7-11370H.
- CPU y modelo comercial de los otros equipos: pendientes; no se requieren para completar la tabla de VRAM.

La RAM y la VRAM son recursos distintos. No se suman ni se considera que las cinco GPUs formen una sola memoria compartida. El consumo real de inferencia debe medirse; el tamaño del modelo en disco no equivale a su uso total de VRAM.

## Reparto inicial propuesto

| Responsable | Función | Modelo o configuración | Estado |
| --- | --- | --- | --- |
| Carlos Delgado | Extracción visual de facturas | `gemma3:4b` | Probado localmente; candidato provisional, evaluación controlada pendiente |
| Carlos Ramos | Chat, enrutamiento y generación de explicaciones según el flujo | Modelo de texto por seleccionar y evaluar | Asignación propuesta |
| Mario | Embeddings para ingesta de documentos y consultas | `embeddinggemma:300m`, 768 dimensiones | Modelo elegido y probado en la laptop de Delgado; ejecución en la laptop de Mario pendiente |
| Juan Pablo | Posible respaldo del servicio de embeddings | Misma versión e identificación de `embeddinggemma:300m` | Pendiente de disponibilidad, instalación y prueba |
| Yael | Pruebas de integración y posible respaldo | Modelo por definir según la necesidad y la capacidad medida | Sin modelo adicional asignado permanentemente |

## Justificación

### Carlos Delgado: visión

Ya tiene instalado `gemma3:4b` y realizó pruebas locales de extracción. Mantener este equipo permite reutilizar la configuración y comparar resultados de forma consistente. Sus 8 GB de VRAM hacen razonable continuar la evaluación, pero no garantizan capacidad para cualquier tamaño de imagen, contexto o concurrencia.

Gemma continúa como candidato provisional debido a errores de lectura y confusión entre campos observados en FATURA. El inventario no modifica esa decisión ni sustituye la evaluación controlada.

### Carlos Ramos: chat

Dispone de 8 GB de VRAM y 40 GB de RAM del sistema. La RAM adicional ofrece margen para el entorno de desarrollo y servicios auxiliares, sin aumentar la VRAM disponible. La asignación también coincide con su responsabilidad sobre el grafo del chat.

No se presupone que su GPU sea más lenta o más rápida que la de Delgado: la potencia configurada, refrigeración y carga influyen en el resultado. La selección de un modelo de texto requiere pruebas propias de enrutamiento, uso de herramientas y respuesta.

### Mario: embeddings

`embeddinggemma:300m` es un modelo de menor tamaño que el candidato de visión: en la descarga observada ocupó 621 MB y produjo vectores de 768 dimensiones. Esto lo convierte en una opción razonable para evaluar en una laptop con 4 GB de VRAM, sin afirmar que ya se midió su consumo o rendimiento allí.

Mario trabaja con las políticas, la ingesta y el RAG. La asignación facilita la integración con ese frente y separa esta carga de visión y chat. Tanto la indexación como las consultas deben usar el mismo modelo y configuración compatibles.

### Juan Pablo y Yael: respaldo y pruebas

Ambos reportan la misma GPU, VRAM y RAM. El inventario no aporta una razón de rendimiento para preferir uno sobre el otro. Se propone inicialmente a Juan Pablo como posible respaldo de embeddings y a Yael para pruebas; pueden intercambiarse según su disponibilidad y carga de trabajo.

El respaldo todavía no está implementado. Su activación requiere instalar y verificar el mismo modelo, comprobar conectividad y establecer cómo cambiar de equipo. No existe conmutación automática acreditada.

## Criterios del reparto

- Separar las cargas principales de visión, chat y embeddings.
- Reutilizar los modelos instalados y las pruebas existentes.
- Priorizar los equipos con 8 GB de VRAM para evaluar las cargas generativas.
- Evitar asignar un modelo diferente a cada laptop únicamente por tener cinco equipos.
- Ajustar el reparto según disponibilidad durante desarrollo y demostración.
- Conectar los servicios según la arquitectura del proyecto mediante Tailscale; la conectividad no se da por configurada con este reporte.

## Evidencia disponible y verificaciones pendientes

**Disponible:** inventario de cinco GPUs; prueba local de visión con resultados y limitaciones documentados; prueba inicial de embeddings en el equipo de Delgado.

**Antes de operar el reparto:**
- Confirmar con cada responsable la asignación y sus horarios de disponibilidad.
- Ejecutar cada modelo en su equipo propuesto y registrar su etiqueta e identificación.
- Medir carga de CPU/GPU, RAM/VRAM, tiempo de respuesta y errores con entradas representativas.
- Verificar conectividad desde otra máquina autorizada del tailnet.
- Evaluar calidad de visión con el mismo prompt y configuración sobre al menos 20 facturas, conforme a S1-26.
- Seleccionar y evaluar el modelo de texto del chat.
- Probar el cambio al respaldo antes de depender de él en la demostración.

## Resultado para S1-25

Quedan documentadas las especificaciones reportadas de las cinco laptops y un reparto de modelos por función con justificación. Esto satisface el alcance documental de S1-25. La instalación, la disponibilidad, las pruebas de rendimiento y la selección definitiva de visión y chat permanecen como trabajo posterior.

## Enlaces

- [[tec/data-steward-agentico/tareas/carlos-delgado|Tareas de Carlos Delgado]]
- [[tec/data-steward-agentico/modelos/decision-modelo-vision-gemma3|Candidato de visión]]
- [[tec/data-steward-agentico/modelos/decision-modelo-embeddings-embeddinggemma|Selección de embeddings]]
- [[tec/data-steward-agentico/modelos/mismo-modelo-de-embeddings|Compatibilidad entre indexación y consultas]]
- [[tec/data-steward-agentico/modelos/decision-inferencia-en-laptops|Inferencia en laptops]]
