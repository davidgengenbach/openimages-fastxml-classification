#!/usr/bin/env bash

INPUT="$1"
FOLDS="$2"

if [ -z "$INPUT" ] || [ -z "$FOLDS"]; then
    echo "Usage: $0 input.txt folds"
    exit 1
fi

LINE_COUNT=$(cat $INPUT | wc -l)

echo "YES${LINE_COUNT}YES"