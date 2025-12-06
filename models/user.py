from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    '''representa un usuario simple en el sitema'''
    nombre: str
    edad: int
    id: Optional[int] = None  #ID asignado automaticamente 
