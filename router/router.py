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


fechas=[
    {
        "codFecha":1,
        "horasParticulares":12,
        "timeStamp":"15/02/2008"
    },
    {
        "codFecha":2,
        "horasParticulares":123,
        "timeStamp":"15/04/2008"
    }
]

@user.get("/tarea")
async def get_tareas() -> list[TareaSchema]:
    lista_de_tareas = tareas_model_get_tareas()
    return lista_de_tareas
    #CODIGO ANTES DE REFACTOR:
    # codTarea, titulo = 0, 1
    # with engine.connect() as conn:
    #     result = conn.execute(tareas.select()).fetchall()
    #     result = [{"codTarea":fila[codTarea], "nombre":fila[titulo]} for fila in result]
    #     return lista_de_tareas

@user.get("/tarea/{codTarea}")
async def get_tarea(codTarea: int) -> TareaSchema:
    tarea = tareas_model_get_tarea(codTarea)
    return tarea
    #CODIGO ANTES DE REFACTOR
    # with engine.connect() as conn:
    #     result = conn.execute(tareas.select().where(tareas.c.codTarea==codTarea)).first()
    #     result = {"codTarea":codTarea, "titulo":result[titulo]}
    #     return result

@user.post("/tarea", status_code=HTTP_201_CREATED)
async def create_tarea(data_tarea: TareaSchema) -> TareaSchema:
    tarea = tareas_model_create_tarea(data_tarea)
    return tarea
    #CODIGO ANTES DE REFACTOR
    # with engine.connect() as conn:
    #     new_tarea=data_tarea.dict()
    #     conn.execute(tareas.insert().values(new_tarea))
    #     return Response(status_code=HT--TP_201_CREATED)
    
@user.put("/tarea/{codTarea}")
async def update_tarea(updatedTarea:TareaSchema) -> TareaSchema:
    tarea = tareas_model_update(updatedTarea)
    return tarea
    #CODIGO ANTES DE REFACTOR
    # with engine.connect() as conn:
    #     conn.execute(tareas.update().values(titulo=updatedTarea.titulo).where(tareas.c.codTarea == codTarea))
    #     result = conn.execute(tareas.select().where(tareas.c.codTarea == codTarea)).first()
    #     result = {"codTarea":codTarea, "titulo": result[titulo]}
    #     return result

@user.delete("/tarea/{codTarea}", status_code=HTTP_204_NO_CONTENT)
def delete_tarea(codTarea:int):
    if (tareas_model_delete(codTarea) >= 1):
        return Response(status_code = HTTP_204_NO_CONTENT)
    else:
        return JSONResponse(status_code=404, content={"message": "La tarea no existe"})
    #CODIGO ANTES DE REFACTOR
    # with engine.connect() as conn:
    #     conn.execute(tareas.delete().where(tareas.c.codTarea == codTarea))
    #     return Response(status_code = HTTP_204_NO_CONTENT)

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
    # with engine.connect() as conn:
    #     result = conn.execute(bloques_laborales.select()).fetchall()
    #     print(result)
    #     result_as_json = [{"codBloqueLaboral":bloque[codBloqueLaboral], "codTarea":bloque[codTarea],
    #               "legajo": bloque[legajo], "horasDelBloque": bloque[horasDelBloque],
    #               "fecha": bloque[fecha]} for bloque in result]

@user.post("/bloque_laboral", status_code=HTTP_201_CREATED)
async def create_bloque(data_bloque_laboral:BloqueLaboralSchema) -> BloqueLaboralSchema:
    if bloques_model_horas_del_recurso(data_bloque_laboral) + data_bloque_laboral.horasDelBloque > 8:
        return JSONResponse(status_code=403, content={"message": "No puedes añadir más de 8 horas en un día para un recurso"})
    bloque = bloques_model_create(data_bloque_laboral)
    return bloque
    # with engine.connect() as conn:
    #     conn.execute(bloques_laborales.insert().values(data_bloque_laboral.dict()))
    #     return Response(status_code=HTTP_201_CREATED)
    

"""

@user.post("/recurso")
def create_recurso(data_recurso:RecursoSchema, status_code=HTTP_201_CREATED):
    with engine.connect() as conn:
        new_recurso=data_recurso.dict()
        conn.execute(recursos.insert().values(new_recurso))
        return Response(status_code=HTTP_201_CREATED)

@user.get("/fechas/{id}")
def get_fechas():
    return list(filter(lambda item:item['codTarea']==id,fechas))
    """