FROM ubuntu:18:04

MAINTAINER zabenno

RUN apt update && apt install -y \
	nginx

COPY --chmod=555 startup-nginx.sh /bin/startup-nginx.sh
COPY --chmod=666 reverse-proxy.conf /etc/nginx/sites-available/reverse-proxy.conf

RUN ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
RUN rm /etc/nginx/sites-enabled/default

ENTRYPOINT /bin/bash startup-nginx.sh
