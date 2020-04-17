FROM ubuntu:18:04

MAINTAINER zabenno

RUN apt update && apt install -y \
	nginx

COPY startup-nginx.sh /bin/startup-nginx.sh
RUN chmod 555 /bin/startup-nginx.sh
COPY reverse-proxy.conf /etc/nginx/sites-available/reverse-proxy.conf
RUN chmod 666 /etc/nginx/sites-available/reverse-proxy.conf

RUN ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
RUN rm /etc/nginx/sites-enabled/default

ENTRYPOINT /bin/bash startup-nginx.sh
