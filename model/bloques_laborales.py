from __future__ import annotations
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql import text
from config.db import engine, meta_data
from schema.bloque_laboral_schema import BloqueLaboralSchema
from fastapi import HTTPException

bloques_laborales=Table("bloques_laborales", meta_data,
               Column("codBloqueLaboral",Integer, primary_key=True),
               Column("codProyectoDeLaTarea",Integer, nullable=False),
               Column("codTarea", Integer, nullable=False),
               Column("legajo", Integer, nullable=False),
               Column("horasDelBloque", Integer, nullable=False),
               Column("fecha", DateTime, nullable=False)
               )
meta_data.create_all(engine)

def bloques_model_horas_del_recurso(data_bloque_laboral: BloqueLaboralSchema):
    try:
        with engine.connect() as conn:
            bloque_nuevo = data_bloque_laboral.dict()
            horas_cargadas_en_usuario = list(conn.execute(
                text(f"""
                SELECT SUM(horasDelBloque) 
                FROM bloques_laborales 
                WHERE legajo={bloque_nuevo['legajo']} AND fecha='{bloque_nuevo['fecha']}';
                """)))[0][0]
            return 0 if not horas_cargadas_en_usuario else horas_cargadas_en_usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al cargar las horas laborales")

def bloques_model_create(data_bloque_laboral: BloqueLaboralSchema):
    try:
        with engine.connect() as conn:
            bloque_nuevo = data_bloque_laboral.dict()
            result = conn.execute(bloques_laborales.insert().values(bloque_nuevo))
            bloque_nuevo["codBloqueLaboral"] = result.inserted_primary_key
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
                                "codProyectoDeLaTarea":item.codProyectoDeLaTarea,\
                                "legajo": item.legajo,\
                                "horasDelBloque": item.horasDelBloque,\
                                "fecha": item.fecha})
            return bloques
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al recuperar las horas laborales")
    

def bloques_model_update(updatedBloqueLaboral: BloqueLaboralSchema):
    try:
        with engine.connect() as conn:
            conn.execute(bloques_laborales.update().values(codTarea=updatedBloqueLaboral.codTarea,
                                                           codProyectoDeLaTarea=updatedBloqueLaboral.codProyectoDeLaTarea,
                                                           legajo=updatedBloqueLaboral.legajo,
                                                           horasDelBloque=updatedBloqueLaboral.horasDelBloque,
                                                           fecha=updatedBloqueLaboral.fecha
                                                           ).where(bloques_laborales.c.codBloqueLaboral == updatedBloqueLaboral.codBloqueLaboral))
            item = conn.execute(bloques_laborales.select().where(bloques_laborales.c.codBloqueLaboral == updatedBloqueLaboral.codBloqueLaboral)).first()
            result = {"codBloqueLaboral":item.codBloqueLaboral,
                    "codProyectoDeLaTarea": item.codProyectoDeLaTarea,
                    "codTarea":item.codTarea,
                    "legajo": item.legajo,
                    "horasDelBloque": item.horasDelBloque,
                    "fecha": item.fecha}
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrio un error al actualizar la tarea")

def bloques_model_delete(codBloqueLaboral: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(bloques_laborales.delete().where(bloques_laborales.c.codBloqueLaboral == codBloqueLaboral))
            return result.rowcount
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error al eliminar el bloque")