#!/bin/sh
set -e

echo "Ждём PostgreSQL (db:5432)..."

until python -c "import socket; s = socket.socket(); s.connect(('db', 5432)); s.close()" 2>/dev/null; do
  echo "PostgreSQL ещё не готова — ждём 2 секунды..."
  sleep 2
done

echo "PostgreSQL готова!"

python manage.py migrate --noinput

python create_superuser.py

echo "Запускаем Gunicorn..."
exec gunicorn stripe_test.wsgi:application --bind 0.0.0.0:8000