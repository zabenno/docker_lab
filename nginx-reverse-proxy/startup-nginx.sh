#!/bin/bash
sed -i 's/FQDN/'"$(cat $FQDN_FILE)"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/SERVER_NAME/'"$(cat $SERVER_NAME_FILE)"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/SERVER_PORT/'"$(cat SERVER_PORT_FILE)"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/CRT_FILE/'"$(cat $CRT_FILE_PATH)"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/KEY_FILE/'"$(cat $KEY_FILE_PATH)"'/g' /etc/nginx/sites-available/reverse-proxy.conf

nginx
