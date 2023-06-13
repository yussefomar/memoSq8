from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

recursos=Table("recursos", meta_data,
               Column("codPersona",Integer, primary_key=True),
               Column("nombre", String(255), nullable=False)
               )
meta_data.create_all(engine)