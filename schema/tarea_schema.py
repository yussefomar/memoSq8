from pydantic import BaseModel
from typing import  Optional

class TareaSchema(BaseModel):
    codTarea:Optional[int]
    titulo:str
     