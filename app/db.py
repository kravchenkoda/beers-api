import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

PG_USER = os.environ['PGUSER']
PG_PASSWORD = quote_plus(os.environ['PGPASSWORD'])
PG_DATABASE = os.environ['PGDATABASE']
PG_HOST = os.environ['PGHOST']
PG_PORT = int(os.environ['PGPORT'])

url = URL.create(
    drivername='postgresql',
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT
)

engine = create_engine(url, echo=True)
