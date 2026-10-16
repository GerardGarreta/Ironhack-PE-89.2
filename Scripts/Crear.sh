#!/bin/bash

# Crear la estructura de directorios
echo "Creando estructura de directorios..."
mkdir -p lab-dh-xor/scripts

# Crear el fichero docker-compose.yml
echo "Creando docker-compose.yml..."
cat << 'EOF' > lab-dh-xor/docker-compose.yml
version: '3.8'

services:
  alice:
    image: python:3.11-slim
    container_name: alice
    hostname: alice
    working_dir: /app
    volumes:
      - ./scripts:/app
    networks:
      red-cripto:
        ipv4_address: 172.28.0.20
    tty: true
    stdin_open: true
    restart: always

  bob:
    image: python:3.11-slim
    container_name: bob
    hostname: bob
    working_dir: /app
    volumes:
      - ./scripts:/app
    networks:
      red-cripto:
        ipv4_address: 172.28.0.10
    tty: true
    stdin_open: true
    restart: always

networks:
  red-cripto:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
EOF

# Crear ficheros de placeholders para los scripts
touch lab-dh-xor/scripts/bob_servidor.py
touch lab-dh-xor/scripts/alice_cliente.py

echo "¡Estructura creada con éxito en la carpeta 'lab-dh-xor'!"

# Levantar el entorno y comprobar el estado
echo "Levantando el entorno con Docker Compose..."
cd lab-dh-xor
docker compose up -d

echo "Comprobando que los contenedores están en ejecución..."
docker ps --filter "name=alice" --filter "name=bob"

