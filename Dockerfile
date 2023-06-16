FROM python:3.10-alpine

RUN mkdir /var/bookstore-services

COPY requirements.txt /var/bookstore-services

WORKDIR /var/bookstore-services

RUN pip3 install -r requirements.txt

COPY . /var/bookstore-services

EXPOSE 5000

ENTRYPOINT ["flask", "--app", "bookstore", "run", "--host=0.0.0.0"]
