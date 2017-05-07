#!/usr/bin/env bash

IN=$1
IN_IMAGES=$2


if [ -z "$IN" ] || \
   [ -z "$IN_IMAGES" ]; then
    echo "Usage: $0 features.ids.txt features.txt"
    exit 1
fi

for id in $(sort $IN | uniq -c | sort -r | grep "2 " | cut -d " " -f 8); do
        feature=$(cat $IN_IMAGES | grep -n -m1 "$id")
        line=$(echo $feature | cut -d ":" -f 1)
        line_plus_one=$(($line + 1))
        echo $line $line_plus_one
        #sed -i.bak -e '5,10d;12d' file
        #echo $id, $(echo $feature | cut -d , -f 1)
        #sed -i "/$id,/d" $IN_IMAGES
        #echo $feature >> $IN_IMAGES
done