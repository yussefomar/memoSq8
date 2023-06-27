import requests
import json
from fastapi import APIRouter, Response
from schema.recurso_schema import RecursoSchema
from schema.tarea_schema import TareaSchema
from schema.bloque_laboral_schema import BloqueLaboralSchema
user = APIRouter()
from config.db import engine
from model.recursos import recursos
from model.tareas import *
from model.bloques_laborales import *
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from fastapi.responses import JSONResponse

@user.get("/recurso")
def get_recursos():
    HTTP_200_OK = 200
    API = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.1/m/api/recursos" 
    response = requests.get(API)
    if response.status_code == HTTP_200_OK:
        return response.json()
    else:
        return response.status_code
    

@user.get("/recurso/{legajo}")
def get_recurso(legajo:int):
    HTTP_200_OK = 200
    API = "https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.1/m/api/recursos" 
    response = requests.get(API)
    if response.status_code == HTTP_200_OK:
        recurso = [recurso for recurso in response.json() if recurso["legajo"] == legajo]
        return recurso
    else:
        return response.status_code

@user.get("/bloque_laboral")
async def get_bloques_laborales() -> list[BloqueLaboralSchema]:
    lista_bloques = bloques_model_get()
    return lista_bloques


@user.post("/bloque_laboral", status_code=HTTP_201_CREATED)
async def create_bloque(data_bloque_laboral:BloqueLaboralSchema) -> BloqueLaboralSchema:
    if bloques_model_horas_del_recurso(data_bloque_laboral) + data_bloque_laboral.horasDelBloque > 8:
        return JSONResponse(status_code=403, content={"message": "No puedes añadir más de 8 horas en un día para un recurso"})
    bloque = bloques_model_create(data_bloque_laboral)
    return bloque

@user.delete("/bloque_laboral", status_code=HTTP_204_NO_CONTENT)
async def delete_bloque(codBloqueLaboral: int):
    if (bloques_model_delete(codBloqueLaboral) >= 1):
        return Response(status_code = HTTP_204_NO_CONTENT)
    else:
        return JSONResponse(status_code=404, content={"message": "El bloque no existe"})
    
@user.put("/bloque_laboral/{codBloqueLaboral}")
async def update_bloque_laboral(updatedBloqueLaboral:BloqueLaboralSchema) -> BloqueLaboralSchema:
    bloque_tras_update = bloques_model_update(updatedBloqueLaboral)
    return bloque_tras_update

@user.get("/tarea")
async def get_tareas() -> list[TareaSchema]:
    lista_de_tareas = tareas_model_get_tareas()
    return lista_de_tareas

@user.get("/tarea/{codTarea}")
async def get_tarea(codTarea: int) -> TareaSchema:
    tarea = tareas_model_get_tarea(codTarea)
    return tarea

@user.post("/tarea", status_code=HTTP_201_CREATED)
async def create_tarea(data_tarea: TareaSchema) -> TareaSchema:
    tarea = tareas_model_create_tarea(data_tarea)
    return tarea
    
@user.put("/tarea/{codTarea}")
async def update_tarea(updatedTarea:TareaSchema) -> TareaSchema:
    tarea = tareas_model_update(updatedTarea)
    return tarea

@user.delete("/tarea/{codTarea}", status_code=HTTP_204_NO_CONTENT)
def delete_tarea(codTarea:int):
    if (tareas_model_delete(codTarea) >= 1):
        return Response(status_code = HTTP_204_NO_CONTENT)
    else:
        return JSONResponse(status_code=404, content={"message": "La tarea no existe"})
