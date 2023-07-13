#!/bin/bash

set -e

DB_NAME=$1
DB_USER=$2
DB_PASSWORD=$3

echo "Creating database..."

if sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'" | grep -q 1; then
  echo "User '$DB_USER' already exists."
else
  sudo -u postgres psql -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';"
  echo "User '$DB_USER' created successfully."
fi

if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
  echo "Database '$DB_NAME' already exists."
else
  sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"
  echo "Database '$DB_NAME' created successfully."
fi

sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
echo "Privileges granted successfully."

echo "Database setup completed!"
