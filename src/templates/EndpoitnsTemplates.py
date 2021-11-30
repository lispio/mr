import json
from enum import Enum


class User(Enum):
    user_keys = ['name', 'password', 'email']


class Recipes(Enum):
    AddRecipes = '{"user_id": "None", "recipes_name": "None", "recipes_type": 0, "is_public": None }'
    FindRecipes = {}
    UpdateRecipes = {}
