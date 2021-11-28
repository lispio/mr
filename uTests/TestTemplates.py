from enum import Enum


class CommonTests(Enum):
    User = {"name": "TestUser", "password": "TestPassword", "email": "Test@email"}
    AddUserRequest = b'{"name": "TestUser", "password": "TestPassword", "email": "Test@email"}'
    CountUsers = "select count(*) from users"
    CountUserName = "select count(name) from users WHERE name LIKE '%s'" % User["name"]
    DeleteTestUser = "DELETE FROM users WHERE name LIKE '%s'" % User["name"]


class ValidateDataTests(Enum):
    TestDict = {"Test1": "test1"}
    TestUserKeys = ['name', 'password', 'email']
    TestAddUserRequest = {"name": "te2", "password": "pass2", "email": "some@email2"}
    TestUserData = ['te2', 'pass2', 'some@email2']
