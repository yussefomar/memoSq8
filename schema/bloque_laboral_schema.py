from pydantic import BaseModel, validator
from typing import  Optional
from datetime import datetime
from model.tareas import tareas_model_get_tarea

class BloqueLaboralSchema(BaseModel):
    codBloqueLaboral:Optional[int]
    codTarea:int
    legajo:int
    horasDelBloque:int
    fecha: datetime

    @validator('codBloqueLaboral')
    def validate_codBloqueLaboral(cls, codBloqueLaboral):
        if codBloqueLaboral is not None and codBloqueLaboral <= 0:
            raise ValueError("El valor de codBloqueLaboral debe ser mayor que 0")
        return codBloqueLaboral

    @validator('horasDelBloque')
    def validate_horasDelBloque(cls, horasDelBloque):
        if horasDelBloque < 0:
            raise ValueError("El valor de horasDelBloque debe ser mayor o igual a 0")
        return horasDelBloque

    @validator('legajo')
    def validate_legajo(cls, legajo):
        if legajo <= 0:
            raise ValueError("El valor de legajo debe ser mayor que 0")
        return legajo

    @validator('codTarea')
    def validate_codTarea(cls, codTarea):
        if not existe_codTarea_en_basededatos(codTarea):
            raise ValueError("El código de tarea no existe en la base de datos")
        return codTarea

def existe_codTarea_en_basededatos(codigo_tarea_a_crear: int):
    return (tareas_model_get_tarea(codigo_tarea_a_crear)["codTarea"] == codigo_tarea_a_crear)





     