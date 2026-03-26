from pydantic import BaseModel, ConfigDict

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock:  int

class ProductoResponse(BaseModel):
    id:     int
    nombre: str
    precio: float
    stock:  int

    model_config = ConfigDict(from_attributes=True)
