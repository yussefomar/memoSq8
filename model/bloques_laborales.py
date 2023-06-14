from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import engine, meta_data

bloques_laborales=Table("bloques_laborales", meta_data,
               Column("codBloqueLaboral",Integer, primary_key=True),
               Column("codTarea", Integer, ForeignKey("tareas.codTarea"), nullable=False),
               Column("legajo", Integer, nullable=False),
               Column("horasDelBloque", Integer, nullable=False),
               Column("fecha", DateTime, nullable=False)
               )
meta_data.create_all(engine)