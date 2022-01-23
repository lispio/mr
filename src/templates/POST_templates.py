from typing import Optional, Set, List
from pydantic import BaseModel


class AddUserIn(BaseModel):
    name: str


class AddUserOut(BaseModel):
    name: str
    status: str


class StepsIn(BaseModel):
    s_num: int = None
    s_desc: str = None


class MingIN(BaseModel):
    ming_id: int
    weight: int


class RecipesIn(BaseModel):
    name: str
    user_id: int
    recipes_type: int
    is_public: bool = False
    des: Optional[str] = None
    steps: List[StepsIn] = None
    ming: List[MingIN] = None


class RecipesOut(BaseModel):
    name: str
    status: str


class StepsUpdate(BaseModel):
    recipes_id: int
    step_id: int

