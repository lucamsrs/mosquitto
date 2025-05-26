FROM eclipse-mosquitto:2.0

# Criar diretórios necessários
RUN mkdir -p /mosquitto/config /mosquitto/data /mosquitto/log

# Copiar configuração
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Definir permissões
RUN chown -R mosquitto:mosquitto /mosquitto/

# Expor portas
EXPOSE 1883 9001

# Comando inicial com verbose para debug
CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf", "-v"]