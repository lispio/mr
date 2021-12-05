from typing import Optional
from pydantic import BaseModel


class AddUser(BaseModel):
    name: str
    password: str
    email: str


class RecipesInOut(BaseModel):
    name: str
    user_id: int
    recipes_type: int
    is_public: bool = False
    des: Optional[str] = None
