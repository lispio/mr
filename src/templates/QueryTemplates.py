from enum import Enum


class qtUsers(Enum):
    insertUsers = "INSERT INTO users (name, password, email) VALUES ('%s', '%s', '%s')"
    getUsers = "SELECT * FROM users"


class qtRecipes(Enum):
    addRecipes = ""
    GetRecipes = "SELECT * FROM recipes"