from fastapi import APIRouter, HTTPException
from services.comision_service import (
    obtener_comisiones_por_vendedor,
    marcar_comision_pagada
)

router = APIRouter(
    prefix="/comisiones",
    tags=["Comisiones"]
)


@router.get("/vendedor/{id_vendedor}")
def ver_comisiones(id_vendedor: int):
    """
    Devuelve todas las comisiones de un vendedor.
    """

    try:
        comisiones = obtener_comisiones_por_vendedor(id_vendedor)

        if not comisiones:
            return {"mensaje": "El vendedor no tiene comisiones registradas."}

        return comisiones

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/pagar/{id_comision}")
def pagar_comision(id_comision: int):
    """
    Marca una comisión como pagada.
    """

    try:
        resultado = marcar_comision_pagada(id_comision)

        if not resultado:
            raise HTTPException(
                status_code=404,
                detail="Comisión no encontrada."
            )

        return {
            "mensaje": "Comisión marcada como pagada correctamente",
            "comision": resultado
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
