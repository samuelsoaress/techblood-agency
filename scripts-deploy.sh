#! /bin/bash

gunzip techblood-agency.tar.gz
docker load -1 techblood-agency.tar

mv docker-compose-prod.yaml docker-compose.yaml

container_ids=$(docker ps -q)

if [ -z "$container_ids" ]; then
  echo "Nao ha containers em execucao"
else
  for container_id in $container_ids; do
    echo "Parando container: $container_id"
    docker stop $container_id
  done
  echo "Todos os containers em execucao foram parados. "
fi 

docker-compose up -d
