from pydantic import BaseModel

class VentaCreate(BaseModel):
    id_vehiculo: int
    id_vendedor: int
    nombre_cliente: str
    cantidad: int
    descuento: float = 0
