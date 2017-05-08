#!/usr/bin/env bash

IN=$1
IN_IMAGES=$2


if [ -z "$IN" ] || \
   [ -z "$IN_IMAGES" ]; then
    echo "Usage: $0 features.ids.txt features.txt"
    exit 1
fi
lines=""
for id in $(sort $IN | uniq -c | sort -r | grep -v " 1 " | cut -d " " -f 8); do
        feature=$(cat $IN | grep -n -m1 "$id")
        #echo $id
        line=$(echo $feature | cut -d ":" -f 1)
        echo $line
        line_plus_one=$(($line + 1))
        lines="$lines $line"
        #lines="$lines;${line},${line_plus_one}d"
        #echo $line $line_plus_one
        #sed -i -e "${line},${line_plus_one}d" $IN_IMAGES
        #echo $id, $(echo $feature | cut -d , -f 1)
        #sed -i "/$id,/d" $IN_IMAGES
        #echo $feature >> $IN_IMAGES
done

#echo $lines
