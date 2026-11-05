---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 6, registro de solo lectura de todo lo que hacen las personas y el agente, con filtros, exportación y filas expandibles.
---
# Pantalla 6: bitácora

## Contenido
- Filtros por caso, usuario, tipo de acción y fecha. Botón **Exportar**.
- Columnas: fecha y hora, caso, quién (persona o agente, con ícono distinto), acción, detalle, regla y versión.
- Cada fila se expande: explicación, valor anterior y nuevo (en correcciones), ID del evento y origen.
- Sin botones de editar ni eliminar.

## Tipos de acción
Extracción de datos · Regla aplicada · Corrección de dato · Escalamiento · Confirmación · Error de procesamiento.

## Para implementar
- Tabla de eventos de solo inserción en PostgreSQL, separada de los checkpoints de LangGraph ([[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|decisión]]).

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
