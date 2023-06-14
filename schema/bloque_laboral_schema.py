from pydantic import BaseModel
from typing import  Optional
from datetime import datetime
class BloqueLaboralSchema(BaseModel):
    codBloqueLaboral:Optional[int]
    codTarea:int
    legajo:int
    horasDelBloque:int
    fecha: datetime
     