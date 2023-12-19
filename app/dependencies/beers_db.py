from os import environ
from urllib.parse import quote_plus

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

PG_USER = environ['PGUSER_BEERS']
PG_PASSWORD = quote_plus(environ['PGPASSWORD_BEERS'])
PG_DATABASE = environ['PGDATABASE_BEERS']
PG_HOST = 'postgres-beers'
PG_PORT = int(environ['PGPORT'])

url = URL.create(
    drivername='postgresql',
    username=PG_USER,
    password=PG_PASSWORD,
    database=PG_DATABASE,
    host=PG_HOST,
    port=PG_PORT
)

engine = create_engine(url, echo=True)
metadata = MetaData(schema='beer')
BeerBase = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
