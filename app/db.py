import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base

PG_USER = os.environ['PGUSER']
PG_PASSWORD = quote_plus(os.environ['PGPASSWORD'])
PG_DATABASE = os.environ['PGDATABASE']
PG_HOST = os.environ['PGHOST']
PG_PORT = int(os.environ['PGPORT'])

metadata = MetaData(schema='beer')
Base = declarative_base(metadata=metadata)

url = URL.create(
    drivername='postgresql',
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)

engine = create_engine(url, echo=True)
