FROM python:3.7-alpine

# Installing necessary components
RUN apk update
RUN apk add musl-dev build-base mariadb-dev linux-headers bash
RUN python -m pip install --upgrade pip

COPY . ./webfoot
WORKDIR /webfoot

RUN pip install -r ./requirements.txt