#!/bin/bash

# Tạo CSDL
kong migrations bootstrap

# Khởi chạy Kong API Gateway
kong start -v
