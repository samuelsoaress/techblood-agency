#! /bin/bash

if [ -f techblood-agency.tar ]; then
  rm techblood-agency.tar
fi
gunzip techblood-agency.tar.gz
echo "Carregando imagem no Docker..."
gzip -d techblood-agency.tar.gz

if [ $? -ne 0 ]; then
  echo "Erro ao descompactar o arquivo techblood-agency.tar.gz"
  exit 1
fi
echo "Descompactado com sucesso"
echo "Carregando imagem no Docker..."
docker load -i techblood-agency.tar

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

echo "Subindo containers"
docker compose up -d
