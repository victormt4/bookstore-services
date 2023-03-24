FROM python:3.10-alpine

RUN mkdir /var/bookstore-services

COPY requirements.txt /var/bookstore-services

WORKDIR /var/bookstore-services

RUN pip3 install -r requirements.txt

COPY . /var/bookstore-services