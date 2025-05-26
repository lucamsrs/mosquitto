FROM eclipse-mosquitto:2.0

# Criar diretório de configuração
RUN mkdir -p /mosquitto/config

# Arquivo de configuração personalizado
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Criar arquivo de senhas
RUN mkdir -p /mosquitto/data
RUN touch /mosquitto/data/passwd

# Definir usuário
RUN mosquitto_passwd -b /mosquitto/data/passwd iot_user secure_password_123

# Expor portas
EXPOSE 1883 9001

# Comando inicial
CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]