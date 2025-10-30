FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ARG CONSUL_VERSION=1.20.1
# RUN wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip && \
#     unzip consul_${CONSUL_VERSION}_linux_amd64.zip && \
#     mv consul /usr/local/bin/ && \
#     rm consul_${CONSUL_VERSION}_linux_amd64.zip && \
#     mkdir -p /consul/data /consul/config

# COPY node-consul-client.template.json /node-consul-client.template.json
# COPY service.template.json /service.template.json
# COPY services_discovery.sh /services_discovery.sh
# RUN chmod +x /services_discovery.sh

COPY registry_api_gateway.sh /registry_api_gateway.sh
RUN chmod +x /registry_api_gateway.sh

COPY start_service.sh /start_service.sh
RUN chmod +x /start_service.sh

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/start_service.sh"]
