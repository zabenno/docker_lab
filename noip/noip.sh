#!/bin/bash

#Check for username docker swarm secret.
if [ -z "$USERNAME_FILE"]
then
	username=$(cat $2)
else
	username="$2"
fi

#Check for password docker swarm secret.
if [ -z "$PASSWORD_FILE"]
then
	password=$(cat $3)
else
	password="$3"
fi

#Create noip configuration file.
noip2 -C -Y -U $1 -u $username -p $password
noip2
while :
do
	sleep 3000
done
