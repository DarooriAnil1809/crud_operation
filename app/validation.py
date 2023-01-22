from pydantic import BaseModel


class UserValidation(BaseModel):
    email: str
    first_name: str
    last_name: str
    is_active = bool

    class Config:
        orm_mode = True
