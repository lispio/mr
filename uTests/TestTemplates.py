from enum import Enum


class CommonTests(Enum):
    CountUsers = "select count(*) from users"
    DeleteTestUser = "DELETE FROM users WHERE name LIKE 'TestUser'"
    User = {"name": 'TestUser', "password": 'TestPassword', "email": 'Test@email'}


