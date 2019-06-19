#!/bin/sh

set -e

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# migrate db and start django
cd /app

python manage.py migrate

# create superuser
if [ -n "$ADMIN_USERNAME" ] && \
    [ -n "$ADMIN_PASSWORD" ] && \
    [ -n "$ADMIN_EMAIL" ] ;
then
    echo "Create superuser: ${ADMIN_USERNAME}"
    python manage.py shell -c "from django.contrib.auth.models import User; \
        User.objects.create_superuser(\
        '${ADMIN_USERNAME}', \
        '${ADMIN_EMAIL}', \
        '${ADMIN_PASSWORD}' \
        )"
fi

exec python manage.py runserver 0.0.0.0:8000

