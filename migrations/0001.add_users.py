steps = [
    step("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY,"
         " name VARCHAR(16) UNIQUE,"
         " password VARCHAR(16), "
         "email VARCHAR(32) UNIQUE);")
]
