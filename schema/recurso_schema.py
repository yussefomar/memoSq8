from pydantic import BaseModel
from typing import  Optional

class RecursoSchema(BaseModel):
    codPersona:Optional[int]
    nombre:str
     