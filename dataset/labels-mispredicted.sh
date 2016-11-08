#!/usr/bin/env bash

set -x

LABELS_IN="download/human_ann_2016_08/validation/labels.csv"
LABELS_OUT="download/human_ann_2016_08/validation/labels_mispredicted.csv"
LABELS_OUT_COUNT="download/human_ann_2016_08/validation/labels_mispredicted_wc.csv"

TMP=$(mktemp)

HEADER="Mispredicted"
cat $LABELS_IN | cut -d , -f 3,4 | grep '0.0' | cut -d , -f 1 | sort > $TMP

# Add header
echo -e "$HEADER\n$(cat $TMP)" > $LABELS_OUT
rm $TMP

cat $LABELS_OUT | ./wordcount.py - > $LABELS_OUT_COUNT