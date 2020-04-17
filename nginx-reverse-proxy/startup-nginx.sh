#!/bin/bash
sed -i "s/FQDN/$FQDN_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "s/SERVER_NAME/$SERVER_NAME_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "s/SERVER_PORT/$SERVER_PORT_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "s/CRT_FILE/$CRT_FILE_PATH/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "s/KEY_FILE/$KEY_FILE_PATH/g" /etc/nginx/sites-available/reverse-proxy.conf

/usr/bin/nginx
