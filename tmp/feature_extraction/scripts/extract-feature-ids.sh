#!/usr/bin/env sh

TMP=$(mktemp)
OUT=features.ids.txt

echo > $TMP

for file in features.fc6.*.txt; do
	if [ "$file" != "features.ids.txt" ]; then
		cat $file | cut -d , -f 1 | grep -v "^$" >> $TMP
	fi
done

grep -v "^$" $TMP > $OUT
