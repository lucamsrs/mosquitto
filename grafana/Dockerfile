FROM grafana/grafana:latest

# Instalar plugins
RUN grafana-cli plugins install grafana-clock-panel
RUN grafana-cli plugins install grafana-simple-json-datasource

# Configurações
ENV GF_SECURITY_ADMIN_USER=admin
ENV GF_SECURITY_ADMIN_PASSWORD=grafana_admin_123
ENV GF_SECURITY_ALLOW_EMBEDDING=true
ENV GF_AUTH_ANONYMOUS_ENABLED=true
ENV GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer

# Copiar configurações personalizadas
COPY grafana-datasources.yml /etc/grafana/provisioning/datasources/
COPY grafana-dashboards.yml /etc/grafana/provisioning/dashboards/
COPY dashboards/ /var/lib/grafana/dashboards/

# Expor porta
EXPOSE 3000

# Volume para dados
VOLUME ["/var/lib/grafana"]