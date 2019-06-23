#!/bin/sh

set -e

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


### FUNCTIONS ###

is_sleep() {
    case "$DEBUG" in
        sleep)
            return 0
            ;;
    esac
    return 1
}

on_exit() {
    exit $RESULT
}

does_db_exist() {
  l_result=$(PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" \
      -U "$PG_ADMIN_USER" \
      -c "SELECT datname FROM pg_catalog.pg_database WHERE datname = '${PG_DB_NAME}';" | \
      sed -n '3s/^[[:space:]]*\('"${PG_DB_NAME}"'\)[[:space:]]*/\1/p')
  test -n "$l_result"
}

does_user_exist() {
  l_result=$(PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" \
      -U "$PG_ADMIN_USER" \
      -c "SELECT rolname FROM pg_catalog.pg_roles WHERE rolname = '${PG_DB_USER}';" | \
      sed -n '3s/^[[:space:]]*\('"${PG_DB_USER}"'\)[[:space:]]*/\1/p')
  test -n "$l_result"
}

wait_for_pg() {
  while ! PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" \
      -U "$PG_ADMIN_USER" -c "\l" >/dev/null 2>&1 ; do
    sleep 2s
  done
}


### SANITY CHECK ###

[ -z "$PG_HOST" ] && echo missing postgres hostname && exit 1
[ -z "$PG_PORT" ] && echo missing postgres port && exit 1
[ -z "$PG_DB_NAME" ] && echo missing postgres db name && exit 1
[ -z "$PG_DB_USER" ] && echo missing postgres db user && exit 1
[ -z "$PG_DB_PASSWORD" ] && echo missing postgres db password && exit 1
[ -z "$PG_ADMIN_USER" ] && echo missing postgres admin user && exit 1
[ -z "$PG_ADMIN_PASSWORD" ] && echo missing postgres admin password && exit 1


### POPULATE DB ###

# start
RESULT=0
trap on_exit INT QUIT TERM EXIT

echo "Wait for postgres to be up..."
wait_for_pg

# ensure that db exists
if ! does_db_exist ; then
    if ! does_user_exist ; then
        echo "Create database user: ${PG_DB_USER}"
        PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_ADMIN_USER" -c \
            "CREATE USER ${PG_DB_USER} WITH PASSWORD '${PG_DB_PASSWORD}';" || \
        {
            echo '[!] ERROR: I cannot create db user' "${PG_DB_USER}"
            RESULT=$?
            exit $?
        }
    fi

    echo "Create database: ${PG_DB_NAME}"

    PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_ADMIN_USER" -c \
        "CREATE DATABASE ${PG_DB_NAME} OWNER ${PG_DB_USER} ${PG_DB_ARGS};" || \
    {
        echo '[!] ERROR: I cannot create db' "${PG_DB_NAME}"
        RESULT=$?
        exit $?
    }

    PGPASSWORD="$PG_ADMIN_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_ADMIN_USER" -c \
        "GRANT ALL PRIVILEGES ON DATABASE ${PG_DB_NAME} to ${PG_DB_USER};" || \
    {
        echo '[!] ERROR: I cannot grant rights for user' "$PG_DB_USER" 'to db' "$PG_DB_NAME"
        RESULT=$?
        exit $?
    }

    if [ -n "$PG_DB_CUSTOM_SCHEMA" ] ; then
        PGPASSWORD="$PG_DB_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_DB_USER" \
            -d "${PG_DB_NAME}" -a -f "$PG_DB_CUSTOM_SCHEMA" || \
        {
            echo '[!] ERROR: I cannot populate db schema'
            RESULT=$?
            exit $?
        }
    fi

    if [ -n "$PG_DB_INITIAL_INSERT" ] ; then
        PGPASSWORD="$PG_DB_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_DB_USER" \
            -d "${PG_DB_NAME}" -a -f "$PG_DB_INITIAL_INSERT" || \
        {
            echo '[!] ERROR: I cannot populate db with initial insert'
            RESULT=$?
            exit $?
        }
    fi
fi


# run default app or command
if [ -z "$1" ] ; then
    exec su portfolio -c /cmd.sh
else
    exec "$@"
fi

