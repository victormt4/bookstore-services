#!/bin/bash

export FLASK_APP=bookstore_services
export FLASK_ENV=development
poetry run flask run
