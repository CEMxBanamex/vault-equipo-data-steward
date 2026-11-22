
# Ejemplo de secuencia SSE del chat

Esta secuencia representa una consulta de facturas en la que el agente
comunica sus pasos antes de entregar la respuesta final.

## 1. Inicio de consulta

event: paso
data: {"id":"paso-1","texto":"Identificando la consulta","detalle":"Clasificando la intención del usuario","estado":"en curso"}

## 2. Actualización del paso

event: paso
data: {"id":"paso-1","texto":"Identificando la consulta","detalle":"Clasificando la intención del usuario","estado":"completado"}

## 3. Nuevo paso

event: paso
data: {"id":"paso-2","texto":"Consultando facturas","detalle":"Buscando registros en la base de datos","estado":"en curso"}

## 4. Finalización del paso

event: paso
data: {"id":"paso-2","texto":"Consultando facturas","detalle":"Se encontraron 12 registros","estado":"completado"}

## 5. Respuesta final

event: respuesta
data: {"contenido":"Se encontraron 12 facturas.","tipo":"datos","fuentes":["facturas"]}
