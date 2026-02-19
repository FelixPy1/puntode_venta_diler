from models.comision_model import (
    insertar_comision,
    obtener_comisiones_por_vendedor
)


def calcular_y_registrar_comision(id_venta: int, id_vendedor: int, total_venta: float):
    """
    Calcula la comisión basada en el total de la venta
    y la registra en la base de datos.
    """

    if total_venta <= 0:
        raise ValueError("El total de la venta debe ser mayor que cero.")

    if id_venta <= 0 or id_vendedor <= 0:
        raise ValueError("IDs inválidos para venta o vendedor.")

    porcentaje = 5.0  # Comisión fija del 5%
    monto = round((total_venta * porcentaje) / 100, 2)

    id_comision = insertar_comision(
        id_venta=id_venta,
        id_vendedor=id_vendedor,
        porcentaje=porcentaje,
        monto=monto
    )

    return {
        "id_comision": id_comision,
        "porcentaje": porcentaje,
        "monto": monto
    }


def listar_comisiones_vendedor(id_vendedor: int):
    """
    Lista todas las comisiones de un vendedor.
    """

    if id_vendedor <= 0:
        raise ValueError("ID de vendedor inválido.")

    comisiones = obtener_comisiones_por_vendedor(id_vendedor)

    return comisiones if comisiones else []
