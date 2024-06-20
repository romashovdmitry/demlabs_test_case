FROM python:3.10.8 as Python

WORKDIR /app

COPY ./Docker/Django_Gunicorn_WSGI/requirements.txt /app
COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt