#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py create_admin
python manage.py bot_setup &
python manage.py collectstatic --no-input

exec gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 5 # --reload --timeout 600

echo 'Django started!'

exec "$@"