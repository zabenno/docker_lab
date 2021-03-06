#!/bin/bash
sed -i 's/FQDN/'"$FQDN"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/SERVER_NAME/'"$SERVER_NAME"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's/SERVER_PORT/'"$SERVER_PORT"'/g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's+CRT_FILE+'"$CRT_FILE_PATH"'+g' /etc/nginx/sites-available/reverse-proxy.conf
sed -i 's+KEY_FILE+'"$KEY_FILE_PATH"'+g' /etc/nginx/sites-available/reverse-proxy.conf

echo "------------------------------------------------"
echo "Using nginx configuration:"
cat /etc/nginx/sites-available/reverse-proxy.conf
echo "------------------------------------------------"

nginx -g 'daemon off;'
