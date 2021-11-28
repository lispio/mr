from enum import Enum


class CommonTests(Enum):
    User = {"name": 'TestUser', "password": 'TestPassword', "email": 'Test@email'}

    CountUsers = "select count(*) from users"
    CountUserName = "select count(name) from users WHERE name LIKE '%s'" % User["name"]
    DeleteTestUser = "DELETE FROM users WHERE name LIKE '%s'" % User["name"]


