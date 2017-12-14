from insuratech.settings import BASE_DIR, DB_HOST

DEBUG = False
TESTING = True
DB_USER = "insuratech-test"
DB_NAME = "insuratech-test"
DB_PASSWORD = "insuratech"
DB_HOST = DB_HOST
DB_PORT = 5432
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

ALEMBIC_CONFIG = "{}/alembic.ini".format(BASE_DIR)
ALEMBIC_MIGRATIONS = "{}/migrations".format(BASE_DIR)
