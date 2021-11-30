steps = [
    step("CREATE TABLE IF NOT EXISTS recipes_type ("
         "rt_id SERIAL PRIMARY KEY, "
         "rt VARCHAR(8) NOT NULL);"),
    step("INSERT INTO recipes_type (rt) VALUES ('bread')"),
    step("INSERT INTO recipes_type (rt) VALUES ('cheese')"),
    step("INSERT INTO recipes_type (rt) VALUES ('wine')"),
    step("INSERT INTO recipes_type (rt) VALUES ('liquor ')"),
]