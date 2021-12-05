steps = [
    step("CREATE TABLE IF NOT EXISTS steps (id SERIAL PRIMARY KEY, "
         "recipes_id SMALLINT,"
         "s_number SMALLINT, "
         "s_desc TEXT, "
         "CONSTRAINT fk_recipes_id FOREIGN KEY (recipes_id) "
         "REFERENCES recipes(id) ON DELETE SET NULL) ;")
]