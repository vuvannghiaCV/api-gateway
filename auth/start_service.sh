#!/bin/sh

/registry_api_gateway.sh
# /services_discovery.sh

alembic upgrade head
python main.py
