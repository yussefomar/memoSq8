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