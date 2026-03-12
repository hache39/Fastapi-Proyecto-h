from pydantic import BaseModel, ConfigDict


# Schema para CREAR un usuario (entrada — sin id)
class UserCreate(BaseModel):
    nombre: str
    edad: int


# Schema para RESPONDER con un usuario (salida — incluye id)
class UserResponse(BaseModel):
    id: int
    nombre: str
    edad: int

    # Permite que Pydantic lea directamente desde objetos SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
