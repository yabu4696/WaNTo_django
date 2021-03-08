#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME \
DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD \
DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL \
python3 manage.py createsuperuser --noinput

celery -A config worker --detach
exec "$@"