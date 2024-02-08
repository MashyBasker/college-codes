#!/usr/bin/bash

# This script is for starting the mysql docker container
STATUS=`sudo systemctl status docker.service | head -n 3 | tail -n 1`
REQUIRED_STATUS="active"

if echo "$STATUS" | grep -q "$REQUIRED_STATUS"; then
	echo 'It is active' ;
else
	echo 'It is inactive';
fi
