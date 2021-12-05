from enum import Enum


class qtUsers(Enum):
    addUsers = "INSERT INTO users (name, password, email) VALUES ('%s', '%s', '%s')"
    getUsers = "SELECT * FROM users WHERE name LIKE '%s'"


class qtRecipes(Enum):
    addRecipes = ""
    getRecipes = "select recipes.name, users.name, recipes_type.rt  from recipes JOIN users ON recipes.user_id = " \
                 "users.id JOIN recipes_type ON recipes.recipes_type = recipes_type.rt_id WHERE recipes.is_public = " \
                 "True;"

    getUserRecipes = "select recipes.name, recipes.recipes_type, recipes.is_public, recipes.des from recipes JOIN " \
                     "users ON recipes.user_id = users.id WHERE users.name = '%s' "
