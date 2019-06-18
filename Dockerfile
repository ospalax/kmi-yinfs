FROM python:3.7-alpine
LABEL maintainer="Petr Ospalý (osp) <petr@ospalax.cz>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install django and dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN apk update && \
 apk add --no-cache \
    postgresql-libs \
    postgresql-client \
    && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
COPY cmd.sh /
RUN chmod +x /cmd.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/cmd.sh"]
