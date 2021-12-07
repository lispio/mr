from typing import Optional
from pydantic import BaseModel


class AddUser(BaseModel):
    name: str
    password: str
    email: str


class RecipesIn(BaseModel):
    name: str
    user_id: int
    recipes_type: int
    is_public: bool = False
    des: Optional[str] = None


class RecipesOut(BaseModel):
    name: str
    status: str

