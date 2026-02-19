from fastapi import APIRouter, HTTPException, status
from schemas.vehiculo_schemas import VehiculoCreate
from services.vehiculo_service import (
    insertar_vehiculo,
    obtener_vehiculos,
    obtener_vehiculo_por_id,
    actualizar_vehiculo,
    eliminar_vehiculo
)

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear(data: VehiculoCreate):
    """
    Crea un nuevo vehículo.
    """
    try:
        id_vehiculo = insertar_vehiculo(data)
        return {
            "mensaje": "Vehículo creado correctamente",
            "id_vehiculo": id_vehiculo
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/")
def listar():
    """
    Lista todos los vehículos.
    """
    try:
        vehiculos = obtener_vehiculos()
        return vehiculos

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/{id_vehiculo}")
def obtener(id_vehiculo: int):
    """
    Obtiene un vehículo por su ID.
    """
    try:
        vehiculo = obtener_vehiculo_por_id(id_vehiculo)

        if not vehiculo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado."
            )

        return vehiculo

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.put("/{id_vehiculo}")
def actualizar(id_vehiculo: int, data: VehiculoCreate):
    """
    Actualiza un vehículo.
    """
    try:
        actualizado = actualizar_vehiculo(id_vehiculo, data)

        if not actualizado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado."
            )

        return {
            "mensaje": "Vehículo actualizado correctamente",
            "vehiculo": actualizado
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.delete("/{id_vehiculo}")
def eliminar(id_vehiculo: int):
    """
    Elimina un vehículo.
    """
    try:
        eliminado = eliminar_vehiculo(id_vehiculo)

        if not eliminado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado."
            )

        return {
            "mensaje": "Vehículo eliminado correctamente",
            "vehiculo": eliminado
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
