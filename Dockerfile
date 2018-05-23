FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install
RUN apt-get update && apt-get install -y netcat postgresql-client
