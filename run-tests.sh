#!/bin/bash

cd docker
docker-compose down
docker-compose build
docker-compose up -d
docker-compose exec app poetry run pytest
docker-compose down
