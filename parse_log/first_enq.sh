#!/usr/bin/env bash

cat acces.log | while read line
do
	flag=$(echo $line | grep -oE "FLAG: .*~"| rev | cut -c 2- | rev | cut -c 20-)
	parsed_flag=$(./parse_url.py <<< $flag)
	if echo $parsed_flag | grep -q "flag"; then echo $flag | awk {"print $4$5"}; fi
done
