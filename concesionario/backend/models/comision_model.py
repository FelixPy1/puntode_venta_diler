from datetime import datetime
from database import get_connection_supabase_client


def insertar_comision(id_venta: int, id_vendedor: int, porcentaje: float, monto: float):
    """
    Inserta una nueva comisión en la tabla 'comisiones'
    y devuelve el id_comision generado.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    data = {
        "id_venta": id_venta,
        "id_vendedor": id_vendedor,
        "porcentaje": porcentaje,
        "monto": monto,
        "pagada": False,
        "fecha": datetime.utcnow().isoformat()  # Quita esto si tu BD tiene DEFAULT NOW()
    }

    response = supabase.table("comisiones").insert(data).execute()

    if response.data and len(response.data) > 0:
        return response.data[0]["id_comision"]

    raise RuntimeError("No se pudo insertar la comisión.")


def obtener_comisiones_por_vendedor(id_vendedor: int):
    """
    Devuelve todas las comisiones de un vendedor.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("comisiones")
        .select("id_comision, porcentaje, monto, pagada, fecha")
        .eq("id_vendedor", id_vendedor)
        .order("fecha", desc=True)
        .execute()
    )

    return response.data if response.data else []


def marcar_comision_pagada(id_comision: int):
    """
    Marca una comisión como pagada.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("comisiones")
        .update({"pagada": True})
        .eq("id_comision", id_comision)
        .execute()
    )

    if not response.data:
        raise RuntimeError("No se encontró la comisión o no se pudo actualizar.")

    return response.data[0]


def obtener_comisiones_pendientes():
    """
    Devuelve todas las comisiones no pagadas.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("comisiones")
        .select("id_comision, id_venta, id_vendedor, porcentaje, monto, fecha")
        .eq("pagada", False)
        .order("fecha", desc=True)
        .execute()
    )

    return response.data if response.data else []
