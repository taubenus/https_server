#!/bin/bash
openssl req -newkey rsa:4096 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
echo "SSL certificate and key generated."
