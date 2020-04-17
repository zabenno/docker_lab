#!/bin/bash
noip2 -C -Y -U $1 -u $2 -p $3
noip2
while :
do
	sleep 3000
done
