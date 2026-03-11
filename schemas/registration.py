from pydantic import BaseModel

class RegistrationCreate(BaseModel):
    user_id: int
    conference_id: int
