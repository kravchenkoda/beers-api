#!/bin/sh

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE PROCEDURE raise_notice (s text)
  LANGUAGE plpgsql as \$$
  begin
      raise notice '%', s;
  end;
  \$$;

	CREATE USER $PGUSER WITH ENCRYPTED PASSWORD '$PGPASSWORD';
	CALL raise_notice('user $PGUSER has been created');
	CREATE ROLE $PGROLE;
	CALL raise_notice('role $PGROLE has been created');
	GRANT $PGROLE TO $PGUSER;
	CREATE DATABASE $PGDATABASE;
	CALL raise_notice('database $PGDATABASE has been created');
  GRANT ALL ON DATABASE $PGDATABASE TO $PGROLE;
EOSQL
