#!/bin/bash
set -e

# Aguardar InfluxDB estar pronto
until influx ping; do
    echo "Aguardando InfluxDB..."
    sleep 2
done

# Criar bucket para IoT se não existir
influx bucket create \
    --name iot_sensors \
    --description "IoT Sensor Data" \
    --retention 30d \
    || echo "Bucket iot_sensors já existe"

# Criar token de acesso
influx auth create \
    --org influxdata \
    --description "IoT Token" \
    --write-bucket iot_sensors \
    --read-bucket iot_sensors \
    || echo "Token já criado"

echo "InfluxDB configurado com sucesso!"