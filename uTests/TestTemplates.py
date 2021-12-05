from enum import Enum


class TUser(Enum):
    uId = 1000
    uName = 'TestUser'
    uPassword = 'TestPassword'
    uEmail = 'Test@email'


class TRecipes(Enum):
    rId = 1000
    rName = 'TestRecipes'
    rType = 1
    ris_public = 'True'


class ResponseGet(Enum):
    UserExist = {'user_id': 1000, 'username': 'TestUser', 'email': 'Test@email'}
    UserNotExist = 'User Not Found'
    RecipesExist = [[1000, 'TestRecipes', 1000, 1, False]]
    RecipesNotExist = 'Recipes Not Found'


class TUQuery(Enum):
    User = {"name": TUser.uName.value, "password": TUser.uPassword.value, "email": TUser.uEmail.value}
    CountUsers = "select count(*) from users"
    CountUserName = "select count(name) from users WHERE name LIKE '%s'" % TUser.uName.value
    TestUserDB = "INSERT INTO users(id, name, password, email) VALUES (%s, '%s', '%s', '%s') " % (TUser.uId.value,
                                                                                                  TUser.uName.value,
                                                                                                  TUser.uPassword.value,
                                                                                                  TUser.uEmail.value)

    DeleteTestUser = "DELETE FROM users WHERE name LIKE '%s'" % TUser.uName.value


class RecipesTests(Enum):
    RecipesOne = "INSERT INTO recipes (id, name, user_id, recipes_type, is_public) " \
                 "VALUES ('%s', '%s', %s, %s, %s)"\
                 % (TRecipes.rId.value, TRecipes.rName.value, TUser.uId.value, TRecipes.rType.value, TRecipes.ris_public.value)

    RecipesUpdate = "UPDATE recipes SET is_public=false WHERE name='%s'" % TRecipes.rName.value
    DeleteRecipes = "DELETE FROM recipes WHERE name LIKE '%s'" % TRecipes.rName.value


class ValidateDataTests(Enum):
    TestDict = {"Test1": "test1"}
    TestUserKeys = ['name', 'password', 'email']
    TestAddUserRequest = {"name": "te2", "password": "pass2", "email": "some@email2"}
    TestUserData = ['te2', 'pass2', 'some@email2']
