# Pydantic schemas for message operations

# Imports
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageCreate(BaseModel):
    """
    Schema for creating a new message.
    """
    message: str = Field(..., min_length=1, max_length=500, description="Message")


class MessageResponse(BaseModel):
    """
    Schema for message response.
    """
    model_config = ConfigDict(from_attributes=True)
    id: int
    message: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class MessageCreateResponse(BaseModel):
    """
    Schema for successful message creation response.
    """
    message: str
    data: MessageResponse
