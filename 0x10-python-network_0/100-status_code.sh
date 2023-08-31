#!/bin/bash
# Sends GET request to given URL and display response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
