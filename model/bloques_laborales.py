from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import engine, meta_data
from schema.bloque_laboral_schema import BloqueLaboralSchema
from fastapi import HTTPException

bloques_laborales=Table("bloques_laborales", meta_data,
               Column("codBloqueLaboral",Integer, primary_key=True),
               Column("codTarea", Integer, ForeignKey("tareas.codTarea"), nullable=False),
               Column("legajo", Integer, nullable=False),
               Column("horasDelBloque", Integer, nullable=False),
               Column("fecha", DateTime, nullable=False)
               )
meta_data.create_all(engine)

def bloques_model_create(data_bloque_laboral: BloqueLaboralSchema):
    try:
        with engine.connect() as conn:
            bloque_nuevo = data_bloque_laboral.dict()
            bloque = conn.execute(bloques_laborales.insert().values(bloque_nuevo))
            return bloque_nuevo
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al cargar las horas laborales")

def bloques_model_get() -> list[BloqueLaboralSchema]:
    try:
        with engine.connect() as conn:
            result = conn.execute(bloques_laborales.select()).fetchall()
            bloques = []
            for item in result:
                bloques.append({"codBloqueLaboral":item.codBloqueLaboral,\
                                 "codTarea":item.codTarea,\
                                "legajo": item.legajo,\
                                "horasDelBloque": item.horasDelBloque,\
                                "fecha": item.fecha})
            print(bloques)
            return bloques
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al recuperar las horas laborales")