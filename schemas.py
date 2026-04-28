from pydantic import BaseModel
from typing import Optional
import datetime

class JobCreate(BaseModel):
    company: str
    role: str
    status: Optional[str] = "applied"
    date_applied: Optional[datetime.date] = None
    notes: Optional[str] = None

class JobResponse(JobCreate):
    id: int

    class Config:
        from_attributes = True