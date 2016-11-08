#!/usr/bin/env sh

set -x
IN=$1

cat $IN/labels_1.csv | ./wordcount.py - | cut -d , -f 2 | ./wordcount.py - > $IN/labels_per_image.csv