# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir jinja2==3.0.3
RUN pip install --no-cache-dir markupsafe==2.1.1
RUN pip install  -r requirements.txt --no-cache-dir

# copy project
COPY . /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh

