#!/bin/sh

PGPASSWORD=$PGPASSWORD psql -h postgres-db -p $PGPORT -U $PGUSER -d $PGDATABASE <<-EOSQL
CREATE SCHEMA IF NOT EXISTS beer;
GRANT ALL ON SCHEMA beer TO $PGROLE;
EOSQL

for sql_script in *;
  do
    PGPASSWORD=$PGPASSWORD psql -h postgres-db -p $PGPORT -U $PGUSER -d $PGDATABASE -f "$sql_script";
  done
echo "Database '$PGDATABASE' has been populated."
