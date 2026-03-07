from pydantic import BaseModel
from datetime import datetime

class ConferenceCreate(BaseModel):
    title: str
    description: str
    location: str
    start_date: datetime
    end_date: datetime