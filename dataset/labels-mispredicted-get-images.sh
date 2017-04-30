#!/usr/bin/env bash

LABELS_MISPREDICTED="download/human_ann_2016_08/validation/labels_mispredicted.csv"

TMP=$(mktemp)
head $LABELS_MISPREDICTED #| cut -d , -f 3,4 | grep '0.0' | cut -d , -f 1 | sort > $TMP
#cat $LABELS_IN | cut -d , -f 1,3,4 | grep '1\.0' > $TMP2
#sed -i '' -e 's/,1.0//g' $TMP2
