#!/usr/bin/env sh

while true; do
	stamp=$(date "+%Y%m%d_%H%M%S")
	done_count=$(wc -l < done.txt)
	echo "$stamp $done_count" >> counts.txt
	sleep 120
done
