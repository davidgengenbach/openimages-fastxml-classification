#!/usr/bin/env bash

LABELS_MISPREDICTED="download/human_ann_2016_08/validation/labels_mispredicted_wc.csv"

ALL_LABELS="download/human_ann_2016_08/validation/labels.csv"
ALL_LABELS_CORRECT="download/human_ann_2016_08/validation/labels_1_3_correct.csv"

for label in $(head -n 10 $LABELS_MISPREDICTED); do
    LABEL=$(echo $label | cut -d , -f 1)
    if [ $(echo $LABEL | grep "word") ]; then
        continue
    fi
    WRONG_COUNT=$(echo $label | cut -d , -f 2)
    RIGHT_COUNT=$(cat $ALL_LABELS_CORRECT | grep "$LABEL" | wc -l)
    RATIO=$(python -c "print($WRONG_COUNT / ($WRONG_COUNT + $RIGHT_COUNT))")

    MISPREDICTED_IMAGES=$(cat $ALL_LABELS | grep $LABEL | grep "0\.0" | cut -d , -f 1)
    SANITIZED_LABEL=$(echo $LABEL | tr "/" "_")
    echo $LABEL $RIGHT_COUNT $WRONG_COUNT $RATIO > download/mispredicted/$SANITIZED_LABEL.txt
    echo $MISPREDICTED_IMAGES >> download/mispredicted/$SANITIZED_LABEL.txt
    #echo $LABEL $WRONG_COUNT $RIGHT_COUNT $(($WRONG_COUNT/$RIGHT_COUNT))
done