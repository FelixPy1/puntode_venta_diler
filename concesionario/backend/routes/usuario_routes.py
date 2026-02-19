from fastapi import APIRouter, HTTPException, status
from schemas.usuario_schemas import UsuarioLogin
from services.usuario_service import login_usuario

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)


@router.post("/login")
def login(usuario: UsuarioLogin):
    """
    Autenticación de usuario.
    """

    try:
        resultado = login_usuario(usuario)

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas."
            )

        return {
            "mensaje": "Login exitoso",
            "usuario": resultado
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
