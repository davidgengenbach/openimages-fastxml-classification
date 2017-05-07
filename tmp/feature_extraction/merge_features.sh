#!/usr/bin/env sh

OUT=$1
shift
IN=$@

if [ -z "$IN" ] || \
   [ -z "$OUT" ]; then
    echo "Usage: $0 feature.ids.txt features.fc8.*.txt"
    exit 1
fi

echo > $OUT

for file in $IN; do
    if [ "$file" != "$OUT" ]; then
        cat $file | grep -v "^$" >> $OUT
    fi
done

sed -i "/^$/d" $OUT