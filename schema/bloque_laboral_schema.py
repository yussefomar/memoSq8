from pydantic import BaseModel, validator
from typing import  Optional
from datetime import datetime
import requests

class BloqueLaboralSchema(BaseModel):
    codBloqueLaboral:Optional[int]
    codProyectoDeLaTarea:int
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
        elif horasDelBloque > 8:
            raise ValueError("No se pueden asignar bloques de más de 8 horas en un día")
        return horasDelBloque

    @validator('legajo')
    def validate_legajo(cls, legajo):
        API = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.1/m/api/recursos" 
        recursos = requests.get(API).json()
        if legajo not in [dict(recurso)["legajo"] for recurso in recursos]:
            raise ValueError("No existe dicho recurso")
        return legajo
    
    @validator('codProyectoDeLaTarea')
    def validate_proyecto(cls, codProyectoDeLaTarea):
        api_call = f"https://tribu-c-proyectos-backend.onrender.com/projects/{codProyectoDeLaTarea}"
        if not requests.get(api_call):
            raise ValueError("No existe el proyecto")
        return codProyectoDeLaTarea






     