#!/bin/bash
# Send a GET request to the URL with custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$1"
