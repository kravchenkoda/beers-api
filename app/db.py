from os import environ
from urllib.parse import quote_plus

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

PG_USER = environ['PGUSER']
PG_PASSWORD = quote_plus(environ['PGPASSWORD'])
PG_DATABASE = environ['PGDATABASE']
PG_HOST = environ['PGHOST']
PG_PORT = int(environ['PGPORT'])

url = URL.create(
    drivername='postgresql',
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)

engine = create_engine(url, echo=True)
metadata = MetaData(schema='beer')
Base = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
