FROM python:3.8.12

RUN mkdir /var/bookstore-services

COPY pyproject.toml /var/bookstore-services
COPY poetry.lock /var/bookstore-services

WORKDIR /var/bookstore-services

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 5000

CMD ["poetry" ,"run","gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120"]