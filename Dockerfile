FROM python:3.7-alpine
LABEL maintainer="osp"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install django and dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN apk update && \
 apk add postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
