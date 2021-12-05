steps = [
    step("CREATE TABLE IF NOT EXISTS recipes (id SERIAL PRIMARY KEY, "
         "name VARCHAR (64) UNIQUE, "
         "user_id SMALLINT, "
         "recipes_type SMALLINT, "
         "desc TEXT, "
         "is_public BOOL DEFAULT false, "
         "CONSTRAINT fk_user_id FOREIGN KEY (user_id) "
         "REFERENCES users(id) ON DELETE SET NULL, "
         "CONSTRAINT fk_recipes_type_rt_id FOREIGN KEY(recipes_type) "
         "REFERENCES recipes_type(rt_id) ON DELETE SET NULL);")
]