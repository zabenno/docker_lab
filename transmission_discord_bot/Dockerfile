FROM python:3.8.2-slim-buster

MAINTAINER zabenno

RUN apt update && apt install -y transmission-remote-cli=1.7.0-1

RUN pip3 install discord.py==1.3.3

COPY discordbot.py /bin/discordbot.py
COPY help.txt /var/cache/help.txt

ENV BOT_TOKEN insert_token_here
ENV T_SERVER localhost
ENV T_PORT 9091
ENV T_USERNAME username
ENV T_PASS password

CMD python3 /bin/discordbot.py
