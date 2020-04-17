#!/bin/bash
sed -i "/FQDN/$FQDN_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "/SERVER_NAME/$SERVER_NAME_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "/SERVER_PORT/$SERVER_PORT_FILE/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "/CRT_FILE/$CRT_FILE_PATH/g" /etc/nginx/sites-available/reverse-proxy.conf
sed -i "/KEY_FILE/$KEY_FILE_PATH/g" /etc/nginx/sites-available/reverse-proxy.conf

/usr/bin/nginx
