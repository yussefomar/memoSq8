from typing import Union

from fastapi import FastAPI

app = FastAPI()

recursos=[
    {
        "codPersona":1,
        "nombre":"jose"

    }
]

tareas=[
    {
        "codTarea":1,
        "titulo":"codificar"

    }
]

fechas=[
    {
        "codFecha":1,
        "horasParticulares":12,
        "timeStamp":"15/02/2008"
    }
]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recursos")
def get_recursos():
    return recursos

@app.get("/tareas")
def get_recursos():
    return tareas

@app.get("/fechas")
def get_recursos():
    return fechas