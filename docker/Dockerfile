FROM python:3.10.8

RUN mkdir /var/bookstore-services

COPY requirements.txt /var/bookstore-services
COPY .env /var/bookstore-services

WORKDIR /var/bookstore-services

RUN pip3 install -r requirements.txt
