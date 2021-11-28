from enum import Enum


class DbInsert(Enum):
    insertUsers = "INSERT INTO users (name, password, email) VALUES ('%s', '%s', '%s')"


class DbGet(Enum):
    GetUsers = "SELECT * FROM users"
