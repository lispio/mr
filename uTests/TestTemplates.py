from enum import Enum


class UserTests(Enum):
    User = {"name": "TestUser", "password": "TestPassword", "email": "Test@email"}
    CountUsers = "select count(*) from users"
    CountUserName = "select count(name) from users WHERE name LIKE 'TestUser'"
    TestUserDB = "INSERT INTO users(id, name, password, email) VALUES (1000, 'TestUser', 'TestUserPassword', 'Test@user')"
    DeleteTestUser = "DELETE FROM users WHERE name LIKE 'TestUser'"


class RecipesTests(Enum):
    RecipesOne = "INSERT INTO recipes (name, user_id, recipes_type) VALUES ('TestRecipes', 1000, 1)"
    DeleteRecipes = "DELETE FROM recipes WHERE name LIKE 'TestRecipes'"


class ValidateDataTests(Enum):
    TestDict = {"Test1": "test1"}
    TestUserKeys = ['name', 'password', 'email']
    TestAddUserRequest = {"name": "te2", "password": "pass2", "email": "some@email2"}
    TestUserData = ['te2', 'pass2', 'some@email2']
