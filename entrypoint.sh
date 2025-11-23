#!/bin/sh
set -e

# Определяем, где мы: на Render (есть DATABASE_URL) или локально (docker-compose)
if [ -n "$DATABASE_URL" ]; then
  echo "Render-режим: используем DATABASE_URL"
  HOST=$(python -c "import urllib.parse, os; print(urllib.parse.urlparse(os.getenv('DATABASE_URL')).hostname)")
  PORT=$(python -c "import urllib.parse, os; print(urllib.parse.urlparse(os.getenv('DATABASE_URL')).port or '5432')")
else
  echo "Локальный режим: ждём db:5432"
  HOST="db"
  PORT="5432"
fi

echo "Ждём PostgreSQL на $HOST:$PORT ..."
until python -c "import socket, time; \
    s=socket.socket(); \
    s.settimeout(2); \
    result=s.connect_ex(('$HOST', $PORT)); \
    s.close(); \
    exit(0 if result==0 else 1)" 2>/dev/null; do
  echo "PostgreSQL ещё не готова — ждём 2 секунды..."
  sleep 2
done

echo "PostgreSQL готова!"

python manage.py migrate --noinput
python create_superuser.py

echo "Запускаем Gunicorn..."
exec gunicorn stripe_test.wsgi:application --bind 0.0.0.0:8000