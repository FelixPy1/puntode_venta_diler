from database import get_connection_supabase_client
import supabase

def obtener_usuario_por_email(email: str):
    response = supabase.table("usuarios") \
        .select("id_usuario, email, password") \
        .eq("email", email) \
        .execute()

    if response.data:
        return response.data[0]  # primer usuario encontrado
    
    return None

