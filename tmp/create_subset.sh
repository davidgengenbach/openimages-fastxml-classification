#!/usr/bin/env bash

NUM_ELEMENTS=$1

if [ "$NUM_ELEMENTS" == "" ]; then
	NUM_ELEMENTS=150000
fi

for f in cpp.fastxml.classes.txt cpp.fastxml.features.txt; do
    echo "Creating subset for: $f"
    head -n $NUM_ELEMENTS $f > small.$f
done

