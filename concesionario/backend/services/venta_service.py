from fastapi import HTTPException, status
from models.venta_model import insertar_venta, actualizar_stock, obtener_vehiculo


def crear_venta(data):
    """
    Crea una venta validando stock y calculando totales.
    """

    if data.cantidad <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La cantidad debe ser mayor que cero."
        )

    if data.descuento < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El descuento no puede ser negativo."
        )

    vehiculo = obtener_vehiculo(data.id_vehiculo)

    if not vehiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehículo no encontrado."
        )

    # Compatible con Supabase (dict) o versión anterior (tupla)
    if isinstance(vehiculo, dict):
        precio = vehiculo.get("precio")
        stock = vehiculo.get("stock")
    else:
        precio, stock = vehiculo

    if data.cantidad > stock:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Stock insuficiente."
        )

    subtotal = round(precio * data.cantidad, 2)
    total = round(subtotal - data.descuento, 2)

    if total < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El total no puede ser negativo."
        )

    venta_data = {
        "id_vehiculo": data.id_vehiculo,
        "id_vendedor": data.id_vendedor,
        "nombre_cliente": data.nombre_cliente,
        "cantidad": data.cantidad,
        "precio_unitario": precio,
        "subtotal": subtotal,
        "descuento": data.descuento,
        "total": total
    }

    id_venta = insertar_venta(venta_data)

    nuevo_stock = stock - data.cantidad
    actualizar_stock(data.id_vehiculo, nuevo_stock)

    return {
        "mensaje": "Venta realizada correctamente",
        "id_venta": id_venta,
        "subtotal": subtotal,
        "total": total,
        "stock_restante": nuevo_stock
    }
