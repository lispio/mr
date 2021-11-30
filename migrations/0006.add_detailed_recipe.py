steps = [
    step("CREATE TABLE IF NOT EXISTS d_recipe (id SERIAL PRIMARY KEY, "
         "recipes_id SMALLINT,"
         "ming_id SMALLINT, "
         "weight SMALLINT, "
         "CONSTRAINT fk_recipes_id FOREIGN KEY (recipes_id) "
         "REFERENCES recipes(id) ON DELETE SET NULL, "
         "CONSTRAINT fk_ming_id FOREIGN KEY(ming_id) "
         "REFERENCES ming(id) ON DELETE SET NULL);")
]