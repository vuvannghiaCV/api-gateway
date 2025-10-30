FROM kong:3.8.0

COPY --from=kong/deck:v1.42.1 /usr/local/bin/deck /usr/local/bin/deck

COPY certs /etc/kong/ssl

COPY config /etc/kong/config

COPY --chmod=+x start_api_gateway.sh /start_api_gateway.sh
# COPY --chmod=775 start_api_gateway.sh /start_api_gateway.sh

CMD ["/start_api_gateway.sh"]
