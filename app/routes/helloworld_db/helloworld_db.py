# Endpoint /helloworld_db - Database operations

# Imports
import logging

# FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Load settings
from app.config.config import Settings

# Database
from app.db.database import get_db
from app.functions.get_settings import get_settings
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageCreateResponse, MessageResponse

# Start Router
router = APIRouter(prefix="/v1")


@router.post(
    "/helloworld_db",
    status_code=status.HTTP_201_CREATED,
    tags=["Hello world DB"],
    response_model=MessageCreateResponse,
    responses={
        201: {
            "description": "Message saved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Message saved successfully",
                        "data": {"id": 1, "message": "Test message", "created_at": "2025-07-12T10:00:00.000Z", "updated_at": None},
                    }
                }
            },
        },
        400: {
            "description": "Validation error",
            "content": {"application/json": {"example": {"detail": "The message must be at least 1 character long"}}},
        },
        500: {
            "description": "Internal server error",
            "content": {"application/json": {"example": {"detail": "Error saving message to the database"}}},
        },
    },
)
def save_message(
    message_data: MessageCreate,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    try:
        logging.info(f"Saving message: {message_data.message}")

        # Crear nueva instancia del modelo Message
        db_message = Message(mensaje=message_data.mensaje)

        # Agregar a la sesión y hacer commit
        db.add(db_message)
        db.commit()
        db.refresh(db_message)

        logging.info(f"Message saved with ID: {db_message.id}")

        # Preparar respuesta
        message_response = MessageResponse.from_orm(db_message)

        return MessageCreateResponse(message="Message saved succesfully", data=message_response)

    except Exception as e:
        logging.error(f"Error saving message to the database: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error saving message to the database")
