from fastapi import APIRouter

user = APIRouter()


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

@user.get("/")
def read_root():
    return {"Hello": "World"}


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