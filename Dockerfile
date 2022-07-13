FROM python:3.10

WORKDIR /app
ADD . /app

RUN python setup.py develop
EXPOSE 8080
