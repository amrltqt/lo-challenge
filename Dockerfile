# pull official base image
FROM python:3.7.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY server/ /usr/src/app/server/
COPY .env.dev /usr/src/app/.env.dev
COPY manage.py /usr/src/app/manage.py