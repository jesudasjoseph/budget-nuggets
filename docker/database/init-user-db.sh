#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER budget_nuggets_user WITH PASSWORD 'dev_password';
	CREATE DATABASE budget_nuggets_db;
	GRANT ALL PRIVILEGES ON DATABASE budget_nuggets_db TO budget_nuggets_user;
	ALTER DATABASE budget_nuggets_db OWNER TO budget_nuggets_user;
	ALTER USER budget_nuggets_user CREATEDB;
EOSQL