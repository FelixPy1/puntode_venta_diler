from database import get_connection_supabase_client

def insertar_vehiculo(data):
    """
    Inserta un vehículo en la tabla 'vehiculos'
    y devuelve el id_vehiculo generado.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    payload = {
        "modelo": data.modelo,
        "marca": data.marca,
        "precio": data.precio,
        "stock": data.stock,
        "estado": data.estado
    }

    response = supabase.table("vehiculos").insert(payload).execute()

    if response.data and len(response.data) > 0:
        return response.data[0]["id_vehiculo"]

    raise RuntimeError("No se pudo insertar el vehículo.")


def obtener_vehiculos():
    """
    Devuelve todos los vehículos.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("vehiculos")
        .select("*")
        .order("id_vehiculo", desc=False)
        .execute()
    )

    return response.data if response.data else []


def obtener_vehiculo_por_id(id_vehiculo):
    """
    Devuelve un vehículo por su ID.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("vehiculos")
        .select("*")
        .eq("id_vehiculo", id_vehiculo)
        .single()
        .execute()
    )

    return response.data if response.data else None


def eliminar_vehiculo(id_vehiculo):
    """
    Elimina un vehículo por su ID.
    """

    supabase = get_connection_supabase_client()

    if supabase is None:
        raise RuntimeError("Supabase no está configurado correctamente.")

    response = (
        supabase
        .table("vehiculos")
        .delete()
        .eq("id_vehiculo", id_vehiculo)
        .execute()
    )

    if not response.data:
        raise RuntimeError("No se encontró el vehículo o no se pudo eliminar.")

    return response.data[0]
