from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    # conference_id: int
    title: str
    description: str
    speaker: str
    start_time: datetime
    end_time: datetime