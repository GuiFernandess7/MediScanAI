#!/bin/sh
/py/bin/python /app/manage.py collectstatic --noinput
/py/bin/python /app/manage.py makemigrations users
/py/bin/python /app/manage.py makemigrations api
/py/bin/python /app/manage.py migrate --run-syncdb
/py/bin/python /app/manage.py runserver #--settings=config.settings.local
