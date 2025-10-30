#!/bin/sh

check_env_variable() {
    local var_name=$1

    local var_value
    var_value=$(eval echo "\$$var_name")

    if [ -z "$var_value" ]; then
        echo "Error: Please set the $var_name environment variable."
        exit 1
    fi

    echo ">>> $var_name = $var_value"
}

check_and_create_dir() {
    local dir_name=$1

    if [ ! -d "$dir_name" ]; then
        echo "Creating directory $dir_name..."
        mkdir -p "$dir_name"
    else
        echo "Directory $dir_name already exists."
    fi
}

check_env_variable "SERVICE_NAME"
check_env_variable "SERVICE_PORT"
check_env_variable "SERVICE_HEALTH_CHECK"

HOSTNAME=$(hostname)

CONSUL_CONFIG_DIR="/consul/config"
check_and_create_dir "$CONSUL_CONFIG_DIR"
CONSUL_DATA_DIR="/consul/data"
check_and_create_dir "$CONSUL_DATA_DIR"

file_config_node_template="/node-consul-client.template.json"
file_config_node="$CONSUL_CONFIG_DIR/node-consul-client.json"
file_config_service_template="/service.template.json"
file_config_service="$CONSUL_CONFIG_DIR/service.json"

envsubst <$file_config_node_template >$file_config_node
envsubst <$file_config_service_template >$file_config_service

nohup consul agent -config-dir=$CONSUL_CONFIG_DIR >/dev/null 2>&1 &
