from enum import Enum


class User(Enum):
    user_keys = ['name', 'password', 'email']


class Recipes(Enum):
    AddRecipes = {}
    FindRecipes = {}
    UpdateRecipes = {}
