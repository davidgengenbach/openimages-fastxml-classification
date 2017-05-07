#!/usr/bin/env sh

TMP=$(mktemp)
OUT=$1
shift
IN=$@

if [ -z "$IN" ] || \
   [ -z "$OUT" ]; then
    echo "Usage: $0 feature.ids.txt features.fc8.*.txt"
    exit 1
fi

echo > $TMP

for file in $IN; do
	if [ "$file" != "$OUT" ]; then
        echo "CurrentFile: $file"
		cat $file | cut -d , -f 1 >> $TMP
	fi
done

grep -v "^$" $TMP > $OUT
