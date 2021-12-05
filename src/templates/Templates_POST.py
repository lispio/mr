from typing import Optional
from pydantic import BaseModel


class AddUser(BaseModel):
    name: str
    password: str
    email: str


class AddRecipes(BaseModel):
    name: str
    user_id: int
    recipes_type: int
    is_public: bool
    des: Optional[str] = None
