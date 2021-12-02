import json
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


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

