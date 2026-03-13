from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    title: str
    description: str
    speaker: str
    start_date: datetime
    end_date: datetime