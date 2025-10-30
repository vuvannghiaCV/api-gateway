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

check_env_variable "KONG_API_GATEWAY_HOST"
check_env_variable "SERVICE_HOST"
check_env_variable "SERVICE_NAME"
check_env_variable "SERVICE_PORT"

microservices_upstream="${SERVICE_NAME}-upstream"
microservices_target="${SERVICE_HOST}:${SERVICE_PORT}"
route_name="${SERVICE_NAME}_route"
route_path="~/api/${SERVICE_NAME}"

create_upstream() {
    echo ">>> Creating upstream '$microservices_upstream'..."

    curl -i -X POST "$KONG_API_GATEWAY_HOST/upstreams" \
        --data "name=$microservices_upstream"
}

create_upstream

create_target() {
    echo ">>> Creating target '$microservices_target'..."

    curl -i -X POST "$KONG_API_GATEWAY_HOST/upstreams/$microservices_upstream/targets" \
        --data "target=$microservices_target" \
        --data "weight=100"

}

create_target

create_service() {
    echo ">>> Creating service '$SERVICE_NAME'..."

    curl -i -X POST "$KONG_API_GATEWAY_HOST/services" \
        --data "name=$SERVICE_NAME" \
        --data "host=$microservices_upstream"

}

create_service

create_route() {
    echo ">>> Creating route '$route_name'..."

    curl -i -s -X POST "$KONG_API_GATEWAY_HOST/services/$SERVICE_NAME/routes" \
        --data "paths[]=$route_path" \
        --data "strip_path=false" \
        --data "name=$route_name"

}
create_route
