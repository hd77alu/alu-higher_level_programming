#!/bin/bash
#A script displays all HTTP methods the server of a given URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
