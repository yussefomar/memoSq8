from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from schema.tarea_schema import TareaSchema
from fastapi import HTTPException

tareas=Table("tareas", meta_data,
               Column("codTarea",Integer, primary_key=True),
               Column("titulo", String(255), nullable=False)
               )
meta_data.create_all(engine)

def tareas_model_create_tarea(data_tarea: TareaSchema):
    try:
        with engine.connect() as conn:
            new_tarea=data_tarea.dict()
            conn.execute(tareas.insert().values(new_tarea))
            return new_tarea
    except Exception as e:
        raise HTTPException(status_code=409, detail="Ya existe una tarea que corresponde a la informacion brindada.")

def tareas_model_get_tareas():
    try:
        with engine.connect() as conn:
            data = conn.execute(tareas.select()).fetchall()
            result = []
            for item in data:
                result.append({"codTarea": item[0], "titulo": item[1]})
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al recuperar las tareas.")

def tareas_model_get_tarea(codTarea: int):
    try:
        with engine.connect() as conn:
            tarea = conn.execute(tareas.select().where(tareas.c.codTarea==codTarea)).first()
            tarea = {"codTarea":tarea.codTarea, "titulo":tarea.titulo}
            return tarea
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al recuperar la tarea")

def tareas_model_update(updatedTarea: TareaSchema):
    try:
        with engine.connect() as conn:
            conn.execute(tareas.update().values(titulo=updatedTarea.titulo).where(tareas.c.codTarea == updatedTarea.codTarea))
            result = conn.execute(tareas.select().where(tareas.c.codTarea == updatedTarea.codTarea)).first()
            result = {"codTarea":result.codTarea, "titulo": result.titulo}
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al actualizar la tarea")

def tareas_model_delete(codTarea: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(tareas.delete().where(tareas.c.codTarea == codTarea))
            return result.rowcount
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error al eliminar la tarea")