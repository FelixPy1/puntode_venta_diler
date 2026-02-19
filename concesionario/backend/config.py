import os

# Configuración mínima para conectar con Supabase.
# Proporciona `SUPABASE_URL` y `SUPABASE_KEY` en variables de entorno.

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def ensure_config():
	"""Lanza un error si falta la configuración requerida."""
	if not SUPABASE_URL or not SUPABASE_KEY:
		raise RuntimeError(
			"Faltan SUPABASE_URL y/o SUPABASE_KEY en las variables de entorno."
		)


__all__ = ["SUPABASE_URL", "SUPABASE_KEY", "ensure_config"]

