from typing import Optional
from pydantic import BaseModel


class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    description: Optional[str] = None


class UserIn(BaseModel):
    username: str

