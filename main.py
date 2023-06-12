from typing import Union

from fastapi import FastAPI

app = FastAPI()

recursos=[
    {
        "codPersona":1,
        "nombre":"jose"

    },
    {
        "codPersona":2,
        "nombre":"martin"

    }
]

tareas=[
    {
        "codTarea":1,
        "titulo":"codificar"

    },
     {
        "codTarea":2,
        "titulo":"compilar"

    }
]

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

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recursos")
def get_recursos():
    return recursos

@app.get("/recursos/{id}")
def get_recursos(id:int):
    return list(filter(lambda item:item['codPersona']==id,recursos))

@app.get("/tareas")
def get_tareas():
    return tareas

@app.get("/tareas/{id}")
def get_tareas():
    return list(filter(lambda item:item['codTarea']==id,tareas))

@app.get("/fechas")
def get_fechas():
    return fechas

@app.get("/fechas/{id}")
def get_fechas():
    return list(filter(lambda item:item['codTarea']==id,fechas))