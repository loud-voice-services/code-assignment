#!/bin/bash

cd nginx
docker build -t nginx .
cd ..
docker build -t bankapi .
docker create network netms
docker-compose up