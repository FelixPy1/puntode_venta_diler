try:
    from supabase import create_client, Client
    from config import SUPABASE_URL, SUPABASE_KEY

    def get_connection_supabase_client() -> Client:
        """
        Devuelve una instancia del cliente Supabase.
        Lanza RuntimeError si faltan variables de entorno.
        """
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise RuntimeError(
                "Faltan SUPABASE_URL y/o SUPABASE_KEY en las variables de entorno."
            )

        return create_client(SUPABASE_URL, SUPABASE_KEY)

except Exception:
    # Si falla la importación de supabase o config
    def get_connection_supabase_client():
        return None
