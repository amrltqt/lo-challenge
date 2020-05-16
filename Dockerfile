# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
COPY server/ /usr/src/app/server/
COPY .env.dev /usr/src/app/.env.dev
COPY manage.py /usr/src/app/manage.py

RUN pip install -r requirements.txt