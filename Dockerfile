FROM python:3.8

LABEL Author="Sergey Romanov"
LABEL E-mail="xxsmotur@gmail.com@gmail.com"
LABEL version="1.0.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "pesto/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /pesto