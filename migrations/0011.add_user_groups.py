steps = [
    step("CREATE TABLE IF NOT EXISTS groups"
         " (id SERIAL PRIMARY KEY,"
         " user_id SMALLINT UNIQUE,"
         " members INTEGER[],"
         " CONSTRAINT fk_user_id FOREIGN KEY (user_id)"
         " REFERENCES users(id) ON DELETE SET NULL);")
]