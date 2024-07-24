FROM python:3.12
ENV PYTHONUNBUFFERED 1

COPY . /project
WORKDIR /project

RUN apt-get update --yes --quiet
RUN pip install -r requirements.txt