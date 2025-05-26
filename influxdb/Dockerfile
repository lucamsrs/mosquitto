FROM influxdb:2.7

# Variáveis de ambiente
ENV INFLUXDB_DB=iot_sensors
ENV INFLUXDB_ADMIN_USER=admin
ENV INFLUXDB_ADMIN_PASSWORD=admin_password_123
ENV INFLUXDB_USER=iot_user
ENV INFLUXDB_USER_PASSWORD=iot_password_123

# Script de inicialização
COPY init-influxdb.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-influxdb.sh

# Expor porta
EXPOSE 8086

# Volume para dados
VOLUME ["/var/lib/influxdb2"]