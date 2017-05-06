#!/usr/bin/env bash

INPUT="$1"
FOLDS="$2"

if [ -z "$INPUT" ] || [ -z "$FOLDS" ]; then
    echo "Usage: $0 input.txt folds"
    exit 1
fi

LINE_COUNT=$(cat $INPUT | wc -l)
ELEMENTS_PER_FOLD=$((${LINE_COUNT} / $FOLDS))


echo "LineCount: $LINE_COUNT"

for i in $(seq 1 $(($FOLDS - 1))); do
    start=$(($i * $ELEMENTS_PER_FOLD))
    end=$(($start + $ELEMENTS_PER_FOLD))
    echo $start / $end
done