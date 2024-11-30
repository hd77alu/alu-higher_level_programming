#!/bin/bash
#a GET request to the URL & display body
curl -s -X GET --header "X-School-User-Id: 98" "$1"
