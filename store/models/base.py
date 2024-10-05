from datetime import datetime
import uuid
from pydantic import BaseModel, Field, UUID4


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(
        default_factory=uuid.uuid4, description="Unique identifier for the product"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the product was created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the product was last updated",
    )

    class Config:
        json_encoders = {
            uuid.UUID: str,  # Converts UUIDs to strings when serializing to JSON
        }
