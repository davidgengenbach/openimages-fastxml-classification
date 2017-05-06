#!/usr/bin/env sh

TMP=$(mktemp)
OUT=features.ids.txt
IN=$@

if [ -z "$IN" ]; then
    echo "Usage: $0 features.fc8.*.txt"
    exit 1
fi

echo > $TMP

for file in $IN; do
	if [ "$file" != "features.ids.txt" ]; then
		cat $file | cut -d , -f 1 | grep -v "^$" >> $TMP
	fi
done

grep -v "^$" $TMP > $OUT
