from pydantic import BaseModel

class VehiculoCreate(BaseModel):
    modelo: str
    marca: str
    precio: float
    stock: int
    estado: str
