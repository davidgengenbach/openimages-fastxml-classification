#!/usr/bin/env bash

LABELS_IN="download/human_ann_2016_08/validation/labels.csv"
LABELS_OUT="download/human_ann_2016_08/validation/labels_mispredicted.csv"
LABELS_OUT_CORRECT_WITH_IMAGEID="download/human_ann_2016_08/validation/labels_1_3_correct.csv"
LABELS_OUT_COUNT="download/human_ann_2016_08/validation/labels_mispredicted_wc.csv"

TMP=$(mktemp)
TMP2=$(mktemp)


# - 1 ImageID
# - 2 Source
# - 3 LabelName
# - 4 Confidence

cat $LABELS_IN | cut -d , -f 3,4 | grep '0\.0' | cut -d , -f 1 | sort > $TMP
#cat $LABELS_IN | cut -d , -f 1,3,4 | grep '1\.0' > $TMP2
#sed -i '' -e 's/,1.0//g' $TMP2

# Add header
echo -e "Mispredicted\n$(cat $TMP)" > $LABELS_OUT
#echo -e "Correct\n$(cat $TMP2)" > $LABELS_OUT_CORRECT_WITH_IMAGEID
rm $TMP $TMP2

cat $LABELS_OUT | ./wordcount.py - > $LABELS_OUT_COUNT

#cat $LABELS_OUT | ./wordcount.py - > $LABELS_OUT_COUNT