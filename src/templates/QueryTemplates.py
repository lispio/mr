# all db request
from enum import Enum


class qtUsers(Enum):
    addUsers = "INSERT INTO users (name) VALUES ('%s')"
    getUsers = "SELECT * FROM users WHERE name LIKE '%s'"


class qtRecipes(Enum):
    addRecipes = "INSERT INTO recipes(name, user_id, recipes_type, is_public, des) " \
                 "VALUES ('%s', %s, %s, '%s', '%s') " \
                 "RETURNING id "

    addRecipesSteps = "INSERT INTO steps(recipes_id, s_number, s_desc) VALUES "

    addRecipesMing = "INSERT INTO recipes_d (recipes_id, ming_id, weight) VALUES "

    getRecipes = "SELECT recipes.id, recipes.name, users.name, recipes_type.rt  FROM recipes " \
                 "JOIN users ON recipes.user_id = users.id " \
                 "JOIN recipes_type ON recipes.recipes_type = recipes_type.rt_id " \
                 "WHERE recipes.is_public = True;"

    getUserRecipes = "SELECT recipes.id, recipes.name, users.name, recipes_type.rt  FROM recipes " \
                     "JOIN users ON recipes.user_id = users.id " \
                     "JOIN recipes_type ON recipes.recipes_type = recipes_type.rt_id " \
                     "WHERE recipes.is_public = True AND users.name = '%s';"

    getMyRecipes = "SELECT recipes.id, recipes.name, users.name, recipes_type.rt  FROM recipes " \
                   "JOIN users ON recipes.user_id = users.id " \
                   "JOIN recipes_type ON recipes.recipes_type = recipes_type.rt_id " \
                   "WHERE users.name = '%s';"

    getRecipesSteps = "SELECT s_number, s_desc FROM steps WHERE recipes_id = (SELECT id FROM recipes WHERE name='%s')"

    getRecipesMing = "SELECT recipes.name, ming.name, recipes_d.weight FROM recipes_d " \
                     "JOIN ming ON recipes_d.ming_id=ming.id " \
                     "JOIN recipes ON recipes_d.recipes_id=recipes.id WHERE " \
                     "recipes.name='%s';"

    updateSteps = "UPDATE steps SET s_desc='%s' WHERE recipes_id=%s AND s_number=%s"


class qtDelete(Enum):
    deleteUser = "DELETE FROM users WHERE name='%s'"
    deleteRecipes = "DELETE FROM recipes WHERE name='%s'"
