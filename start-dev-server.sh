#!/bin/bash

docker build -t victormt4/bookstore-services .
docker run -p 5000:5000 -v $PWD:/var/bookstore-services victormt4/bookstore-services
