from pydantic import BaseModel, validator
from typing import  Optional

class TareaSchema(BaseModel):
    codTarea:Optional[int]
    titulo:str
    
    @validator('codTarea')
    def validate_codTarea(cls, codTarea):
        if codTarea is not None and codTarea <= 0:
            raise ValueError("El valor de codTarea debe ser mayor que 0")
        return codTarea