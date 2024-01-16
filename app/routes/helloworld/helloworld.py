# Endpoint /status

# Imports
import logging

# FastAPI
from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse

# Load settings
from app.config.config import Settings
from app.functions.get_settings import get_settings

# Start Router
router = APIRouter(prefix="/v1")


@router.get(
    "/helloworld",
    status_code=status.HTTP_200_OK,
    tags=["Hello World"],
    responses={
        200: {
            "description": "Successful Response",
            "content": {"application/json": {"example": {"message": "Hello World"}}},
        },
    },
)
def helloworld(
    settings: Settings = Depends(get_settings),
):
    """
        Sends Hello World message
    """
    logging.info("Returning API status")
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Hello World",
        },
    )
