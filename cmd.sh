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
    # if it not already exists...
    if ! python manage.py shell -c "from django.contrib.auth.models import User; \
        users = list(User.objects.values('username')); \
        admin = [user['username'] for user in users if user['username'] == 'admin']; \
        print(admin[0] if len(admin) > 0 else ''); \
        " | grep -q "^${ADMIN_USERNAME}\$" ;
    then
        python manage.py shell -c "from django.contrib.auth.models import User; \
            User.objects.create_superuser(\
            '${ADMIN_USERNAME}', \
            '${ADMIN_EMAIL}', \
            '${ADMIN_PASSWORD}' \
            )"
    fi
fi

exec python manage.py runserver 0.0.0.0:8000

