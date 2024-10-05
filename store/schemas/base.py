from datetime import datetime
import uuid
from pydantic import BaseModel, Field, UUID4


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(
        default_factory=uuid.uuid4, description="Unique identifier for the record"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the record was created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the record was last updated",
    )

    class Config:
        orm_mode = True  # Permite que o Pydantic use instâncias de ORM como entrada
