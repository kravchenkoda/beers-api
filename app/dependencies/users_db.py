from os import environ
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

import app.db_models.users

PG_USER = environ['PGUSER_USERS']
PG_PASSWORD = quote_plus(environ['PGPASSWORD_USERS'])
PG_DATABASE = environ['PGDATABASE_USERS']
PG_HOST = 'postgres-users'
PG_PORT = int(environ['PGPORT'])

url = URL.create(
    drivername='postgresql',
    username=PG_USER,
    database=PG_DATABASE,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)

engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

app.db_models.users.UsersBase.metadata.create_all(bind=engine)
SessionLocal().commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
