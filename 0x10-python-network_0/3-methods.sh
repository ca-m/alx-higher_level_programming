#!/bin/bash
# Display all HTTP methods server of given URL will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
