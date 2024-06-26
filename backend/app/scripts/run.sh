#!/bin/sh

set -e

python /app/manage.py wait_for_db
python /app/manage.py collectstatic --noinput
python /app/manage.py makemigrations users
python /app/manage.py makemigrations api
python /app/manage.py migrate --run-syncdb

uwsgi --socket :9000 --workers 2 --master --enable-threads --module config.wsgi