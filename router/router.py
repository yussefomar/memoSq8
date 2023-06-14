import requests
from fastapi import APIRouter, Response
from schema.recurso_schema import RecursoSchema
from schema.tarea_schema import TareaSchema
user = APIRouter()
from config.db import engine
from model.recursos import recursos
from model.tareas import tareas
from starlette.status import HTTP_201_CREATED


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
def get_tareas():
    codTarea, titulo = 0, 1
    with engine.connect() as conn:
        result = conn.execute(tareas.select()).fetchall()
        result = [{"codTarea":fila[codTarea], "nombre":fila[titulo]} for fila in result]
        return result

@user.get("/tarea/{}")
def get_tarea(codTarea:int):
    codigo, titulo = 0, 1
    with engine.connect() as conn:
        result = conn.execute(tareas.select().where(tareas.c.codTarea==codTarea)).first()
        result = {result[codigo]:result[titulo]}
        return result

@user.post("/tarea")
def create_tarea(data_tarea:TareaSchema, status_code=HTTP_201_CREATED):
    with engine.connect() as conn:
        new_tarea=data_tarea.dict()
        conn.execute(tareas.insert().values(new_tarea))
        return Response(status_code=HTTP_201_CREATED)
    
@user.put("/tarea/{codTarea}")
def update_tarea(updatedTarea:TareaSchema, codTarea:int):
    codigo, titulo = 0, 1
    with engine.connect() as conn:
        conn.execute(tareas.update().values(titulo=updatedTarea.titulo).where(tareas.c.codTarea == codTarea))
        result = conn.execute(tareas.select().where(tareas.c.codTarea == codTarea)).first()
        result = {result[codigo]:result[titulo]}
        return result

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


"""

@user.post("/recurso")
def create_recurso(data_recurso:RecursoSchema, status_code=HTTP_201_CREATED):
    with engine.connect() as conn:
        new_recurso=data_recurso.dict()
        conn.execute(recursos.insert().values(new_recurso))
        return Response(status_code=HTTP_201_CREATED)


@user.get("/recursos")
def get_recursos():
    return recursos

@user.get("/recursos/{id}")
def get_recursos(id:int):
    return list(filter(lambda item:item['codPersona']==id,recursos))

@user.get("/tareas")
def get_tareas():
    return tareas

@user.get("/tareas/{id}")
def get_tareas():
    return list(filter(lambda item:item['codTarea']==id,tareas))

@user.get("/fechas")
def get_fechas():
    return fechas

@user.get("/fechas/{id}")
def get_fechas():
    return list(filter(lambda item:item['codTarea']==id,fechas))
    """