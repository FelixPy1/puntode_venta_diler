from database import get_connection_supabase_client
from datetime import datetime


def insertar_venta(data: dict):
    """
    Inserta una venta en la tabla 'ventas'
    y devuelve el id_venta generado.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    payload = {
        "id_vehiculo": data["id_vehiculo"],
        "id_vendedor": data["id_vendedor"],
        "nombre_cliente": data["nombre_cliente"],
        "cantidad": data["cantidad"],
        "precio_unitario": data["precio_unitario"],
        "subtotal": data["subtotal"],
        "descuento": data["descuento"],
        "total": data["total"],
        "fecha_venta": datetime.utcnow().isoformat()  # Puedes quitar esto si usas DEFAULT NOW()
    }

    response = supabase.table("ventas").insert(payload).execute()

    if response.data and len(response.data) > 0:
        return response.data[0]["id_venta"]

    raise RuntimeError("No se pudo insertar la venta.")


def actualizar_stock(id_vehiculo: int, nueva_cantidad: int):
    """
    Actualiza el stock de un vehículo.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("vehiculos")
        .update({"stock": nueva_cantidad})
        .eq("id_vehiculo", id_vehiculo)
        .execute()
    )

    if not response.data:
        raise RuntimeError("No se encontró el vehículo o no se pudo actualizar el stock.")

    return response.data[0]


def obtener_vehiculo(id_vehiculo: int):
    """
    Obtiene el precio y stock de un vehículo.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("vehiculos")
        .select("precio, stock")
        .eq("id_vehiculo", id_vehiculo)
        .single()
        .execute()
    )

    return response.data if response.data else None
