FROM ubuntu:18.04
MAINTAINER zabenno

#Added dependencies.
RUN apt update && apt install -y \
	wget \
	gcc \
	make \
	curl

#Download, unzip and build NoIP client.
RUN wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz -P /tmp/ && \tar xzf /tmp/noip-duc-linux.tar.gz -C /usr/local/src/ && \
	make -C /usr/local/src/* && \
	cp /usr/local/src/*/noip2 /usr/local/bin/noip2 && \
	rm -rf /usr/local/src/noip*

#Add sleep script so container doesn't die.
COPY noip.sh /usr/local/bin/noip.sh
RUN chmod 555 /usr/local/bin/noip.sh

#Start by launching the service.
ENTRYPOINT /bin/bash noip.sh $REFRESH_INTERVAL $USERNAME $PASSWORD
