#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput
exec gunicorn config.wsgi:application --bind 0:8000