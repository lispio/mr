import json
from enum import Enum
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    description: Optional[str] = None


class UserIn(BaseModel):
    username: str



