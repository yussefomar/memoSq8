from pydantic import BaseModel
from typing import  Optional

class RecursoSchema(BaseModel):
    codPersona:Optional[str]
    nombre:str
     