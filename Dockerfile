FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN mkdir /django_project
WORKDIR /django_project

ADD requirements.txt /django_project/

RUN pip install -r requirements.txt
COPY . /django_project

