FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade && \
    apk add --update --no-cache \
    openssh-client \
    build-base \
    bash \
    git \
    python3-dev \
    py-pip \
    postgresql-dev \
    postgresql-client \
    gettext && \
    rm /var/cache/apk/*

WORKDIR /srv/app

COPY ./docker/scripts/entrypoint.sh \
    ./requirements.txt \
    /srv/app/

RUN apk update && \
    sh ./entrypoint.sh && \
    apk del -r postgresql
