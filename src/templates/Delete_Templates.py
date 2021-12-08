from typing import Optional
from pydantic import BaseModel


class DeleteUserIn(BaseModel):
    username: str


class DeleteUserOut(BaseModel):
    username: str
    status: str


class DeleteRecipesOut(BaseModel):
    username: str
    status: str
