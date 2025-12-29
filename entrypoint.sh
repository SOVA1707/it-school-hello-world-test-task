#!/bin/bash

until poetry run python -c "import psycopg2; psycopg2.connect(
    dbname='$POSTGRES_DB',
    user='$POSTGRES_USER',
    password='$POSTGRES_PASSWORD',
    host='$POSTGRES_HOST',
    port='$POSTGRES_PORT'
)" > /dev/null 2>&1; do
  echo "⏳ Waiting for PostgreSQL to be ready..."
  sleep 5
done

echo "🔄 Applying Django migrations..."
poetry run python manage.py migrate --noinput
echo "✅ Migrations applied successfully."

poetry run python manage.py collectstatic --noinput

exec "$@"