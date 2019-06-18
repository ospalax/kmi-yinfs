#!/bin/sh

set -e

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# migrate db and start django
cd /app

python manage.py migrate

exec python manage.py runserver 0.0.0.0:8000

