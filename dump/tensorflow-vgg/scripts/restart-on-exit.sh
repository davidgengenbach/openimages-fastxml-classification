#!/usr/bin/env sh

POLL_INTERVAL=10
while true; do
    PYTHON_PROCESSES=$(pgrep python3 | wc -l)
    if [ "$PYTHON_PROCESSES" = "0" ]; then
        STAMP=$(date "+%d.%m. %H:%M:%S")
        echo "$STAMP: Restarting processes"
        ./scripts/run-multiple-cluster.sh
    fi
    sleep $POLL_INTERVAL
done