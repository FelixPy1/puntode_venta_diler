from backend.database import get_connection_supabase_client

def obtener_usuario_por_email(email: str):
    supabase = get_connection_supabase_client()

    if not supabase:
        return None

    response = supabase.table("usuarios") \
        .select("*") \
        .eq("email", email) \
        .execute()

    if response.data:
        return response.data[0]

    return None