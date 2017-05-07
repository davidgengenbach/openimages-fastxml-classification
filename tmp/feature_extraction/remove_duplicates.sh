#!/usr/bin/env bash

IN=$1

if [ -z "$IN" ]; then
    echo "Usage: $0 features.ids.txt"
    exit 1
fi

for id in $(sort $IN | uniq -c | sort -r | grep "2 " | cut -d " " -f 8); do
    echo "Yes $id"
done