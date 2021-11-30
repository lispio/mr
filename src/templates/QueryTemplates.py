from enum import Enum


class Users(Enum):
    insertUsers = "INSERT INTO users (name, password, email) VALUES ('%s', '%s', '%s')"
    getUsers = "SELECT * FROM users"


class Recipes(Enum):
    addRecipes = ""
    GetRecipes = ""
