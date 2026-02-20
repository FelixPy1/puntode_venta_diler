from fastapi import APIRouter, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from backend.schemas.usuario_schemas import UsuarioLogin
from backend.models.usuario_model import obtener_usuario_por_email


router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

def login_usuario(data):

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

    # 🔥 AQUÍ VA LO QUE ME PREGUNTASTE

    if isinstance(usuario, dict):
        id_usuario = usuario.get("id_usuario")
        email = usuario.get("email")
        password_db = usuario.get("password")
        rol = usuario.get("rol")
    else:
        id_usuario, email, password_db, rol = usuario

    if data.password != password_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas."
        )

    return {
        "id_usuario": id_usuario,
        "email": email,
        "rol": rol
    }