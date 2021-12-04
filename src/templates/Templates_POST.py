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
    descriptions: Optional[str] = None
    is_public: bool
