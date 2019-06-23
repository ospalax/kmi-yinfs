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
    libpng \
    freetype \
    libjpeg-turbo \
    lcms2 \
    openjpeg \
    tiff \
    libwebp \
    zlib \
    && \
 apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    libpng-dev \
    freetype-dev \
    libjpeg-turbo-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    libwebp-dev \
    zlib-dev \
    && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN mkdir -p /var/www/data

# setup user to run the service
#
# I am aware that setting the GID/UID to 1000 beats the purpose of using the
# system option (-S), but it is annoying to fix the ownership every time I do
# "makemigrations" during the development...
RUN addgroup -S -g 1000 portfolio && \
    adduser -S -u 1000 -G portfolio -h / -HD -s /bin/sh portfolio
RUN chown portfolio:portfolio /var/www/data

# entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
COPY cmd.sh /
RUN chmod +x /cmd.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
#CMD ["/cmd.sh"]
