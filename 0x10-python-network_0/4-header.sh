#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL to send the GET request
url=$1

# Header variable
header="X-School-User-Id: 98"

# Send GET request using curl
response=$(curl -s -H "$header" "$url")

# Display the body of the response
echo "Hello School!"
echo "$response"

