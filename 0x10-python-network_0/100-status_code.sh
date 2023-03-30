#!/bin/bash
#send a GET request to a given URL and display the response status code
curl -s -o /dev/null -w "%{http_code}\n" "$1"
