from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

tareas=Table("tareas", meta_data,
               Column("codTarea",Integer, primary_key=True),
               Column("titulo", String(255), nullable=False)
               )
meta_data.create_all(engine)