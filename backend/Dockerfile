FROM tiangolo/uwsgi-nginx:python3.6

ENV PIP_DISABLE_PIP_VERSION_CHECK on

MAINTAINER Michael Pérez "mpuhrez@gmail.com"

COPY . /app
WORKDIR /app

RUN make setup