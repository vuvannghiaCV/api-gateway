#!/bin/bash

for i in {1..5}; do
  curl -k -X 'GET' \
    'https://localhost:8443/api/user' | jq
done
