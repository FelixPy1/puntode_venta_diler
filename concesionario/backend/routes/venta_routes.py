from fastapi import APIRouter, HTTPException, status
from schemas.venta_schemas import VentaCreate
from services.venta_service import crear_venta

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def registrar_venta(venta: VentaCreate):
    """
    Registra una nueva venta.
    """

    try:
        resultado = crear_venta(venta)

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se pudo registrar la venta."
            )

        return {
            "mensaje": "Venta registrada correctamente",
            "venta": resultado
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
