#!/bin/bash
set -e

echo "Running init.sh script..."

if [ -z "$KONG_PASSWORD_DATABASE" ]; then
    echo "Error: Please set the KONG_PASSWORD_DATABASE environment variable."
    exit 1
fi

POSTGRES="psql --username ${POSTGRES_USER}"

$POSTGRES <<-EOSQL

CREATE EXTENSION IF NOT EXISTS pgcrypto CASCADE;

CREATE USER kong WITH PASSWORD '${KONG_PASSWORD_DATABASE}';
CREATE DATABASE kong OWNER kong;

CREATE DATABASE auth;


EOSQL
