from models.vehiculo_model import insertar_vehiculo


def crear_vehiculo(data):
    """
    Crea un vehículo y define automáticamente su estado
    según el stock disponible.
    """

    if data.stock < 0:
        raise ValueError("El stock no puede ser negativo.")

    # Determinar estado automáticamente
    estado = "VENDIDO" if data.stock == 0 else "DISPONIBLE"

    # Crear un objeto limpio para enviar al modelo
    vehiculo_data = type(data)(
        modelo=data.modelo,
        marca=data.marca,
        precio=data.precio,
        stock=data.stock,
        estado=estado
    )

    id_vehiculo = insertar_vehiculo(vehiculo_data)

    return {
        "mensaje": "Vehículo creado correctamente",
        "id_vehiculo": id_vehiculo,
        "estado": estado
    }
