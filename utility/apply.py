from yoyo import read_migrations, get_backend

backend = get_backend('postgres://it:it@localhost/mr')
migrations = read_migrations('./migrations')
backend.apply_migrations(backend.to_apply(migrations))
