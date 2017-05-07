#!/usr/bin/env sh

DONE_FILE=$1
COUNTS_FILE=$2
INTERVAL=120

if  [ -z "$DONE_FILE" ] || \
    [ -z "$COUNTS_FILE" ]; then
    echo "Usage: $0 done.txt counts.txt"
    exit 1
fi

while true; do
	stamp=$(date "+%Y%m%d_%H%M%S")
	done_count=$(wc -l < $DONE_FILE)
	echo "$stamp $done_count" >> $COUNTS_FILE
	sleep $INTERVAL
done
