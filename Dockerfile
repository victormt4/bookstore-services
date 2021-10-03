FROM python:3.8.12

RUN mkdir /var/bookstore-services

COPY requirements.txt /var/bookstore-services

WORKDIR /var/bookstore-services

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120"]