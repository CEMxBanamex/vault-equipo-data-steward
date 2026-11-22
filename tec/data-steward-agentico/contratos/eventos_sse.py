from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class EstadoPaso(str, Enum):
    PENDIENTE = "pendiente"
    EN_CURSO = "en curso"
    COMPLETADO = "completado"
    ERROR = "error"


class TipoRespuesta(str, Enum):
    DATOS = "datos"
    POLITICAS = "politicas"
    INFORMACION_GENERAL = "informacion_general"
    MIXTA = "mixta"


class PasoEvent(BaseModel):
    id: str
    texto: str
    detalle: Optional[str] = None
    estado: EstadoPaso


class RespuestaEvent(BaseModel):
    contenido: str
    tipo: TipoRespuesta
    fuentes: list[str] = Field(default_factory=list)