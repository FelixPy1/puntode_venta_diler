from models.usuario_model import obtener_usuario_por_email
from fastapi import HTTPException, status


def login_usuario(data):
    """
    Autentica un usuario por email y contraseña.
    """

    if not data.email or not data.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email y contraseña son obligatorios."
        )

    usuario = obtener_usuario_por_email(data.email)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas."
        )

    # Si estás usando Supabase, normalmente devuelve dict
    # Pero si tu model devuelve tupla, mantenemos compatibilidad:

    if isinstance(usuario, dict):
        id_usuario = usuario.get("id_usuario")
        email = usuario.get("email")
        password_db = usuario.get("password")
    else:
        id_usuario, email, password_db = usuario

    if data.password != password_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas."
        )

    return {
        "mensaje": "Login exitoso",
        "id_usuario": id_usuario,
        "email": email
    }
