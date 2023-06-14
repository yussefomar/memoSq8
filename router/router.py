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
from model.bloques_laborales import bloques_laborales
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


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

@user.get("/tarea/{}")
async def get_tarea(codTarea:int) -> TareaSchema:
    tarea = tareas_model_get_tarea(codTarea)
    return tarea
    # with engine.connect() as conn:
    #     result = conn.execute(tareas.select().where(tareas.c.codTarea==codTarea)).first()
    #     result = {"codTarea":codTarea, "titulo":result[titulo]}
    #     return result

@user.post("/tarea", status_code=HTTP_201_CREATED)
async def create_tarea(data_tarea: TareaSchema) -> TareaSchema:
    tarea = tareas_model_create_tarea(data_tarea)
    return tarea
    #CODIGO ANTERIOR A REFACTOR:
    # with engine.connect() as conn:
    #     new_tarea=data_tarea.dict()
    #     conn.execute(tareas.insert().values(new_tarea))
    #     return Response(status_code=HTTP_201_CREATED)
    
@user.put("/tarea/{codTarea}")
def update_tarea(updatedTarea:TareaSchema, codTarea:int):
    codigo, titulo = 0, 1
    with engine.connect() as conn:
        conn.execute(tareas.update().values(titulo=updatedTarea.titulo).where(tareas.c.codTarea == codTarea))
        result = conn.execute(tareas.select().where(tareas.c.codTarea == codTarea)).first()
        result = {"codTarea":codTarea, "titulo": result[titulo]}
        return result

@user.delete("/tarea/{codTarea}", status_code=HTTP_204_NO_CONTENT)
def delete_tarea(codTarea:int):
    with engine.connect() as conn:
        conn.execute(tareas.delete().where(tareas.c.codTarea == codTarea))
        return Response(status_code = HTTP_204_NO_CONTENT)

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
def get_bloques_laborales():
    codBloqueLaboral, codTarea, legajo = 0, 1, 2
    horasDelBloque, fecha = 3, 4
    with engine.connect() as conn:
        result = conn.execute(bloques_laborales.select()).fetchall()
        print(result)
        result_as_json = [{"codBloqueLaboral":bloque[codBloqueLaboral], "codTarea":bloque[codTarea],
                  "legajo": bloque[legajo], "horasDelBloque": bloque[horasDelBloque],
                  "fecha": bloque[fecha]} for bloque in result]
        return result_as_json

@user.post("/bloque_laboral", status_code=HTTP_201_CREATED)
def create_tarea(data_bloque_laboral:BloqueLaboralSchema):
    with engine.connect() as conn:
        conn.execute(bloques_laborales.insert().values(data_bloque_laboral.dict()))
        return Response(status_code=HTTP_201_CREATED)
    

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