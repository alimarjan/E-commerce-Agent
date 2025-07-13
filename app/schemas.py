
from pydantic import BaseModel, Field
from typing import Optional

class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="Customer support message to classify")

class ClassificationResponse(BaseModel):
    input: str
    classification: str
    status: str
    error: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    service: str
