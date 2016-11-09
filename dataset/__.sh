#!/usr/bin/env bash

find download -name '*.png' -exec rm {} \;

find download -name 'labels_3_wc.txt' -exec bash -c 'Rscript labels-distribution.r `dirname {}`' \;
find download -name 'labels_per_image.csv' -exec bash -c 'Rscript labels-per-image-hist.r `dirname {}`' \;
find download -name 'labels_per_image.csv' -exec bash -c './labels-per-image.py `dirname {}`' \;


if [ 0 == 1 ]; then
    find . -name 'labels_3_wc.txt' -exec bash -c 'Rscript labels-distribution.r `dirname {}`' \;
    find . -name 'labels_per_image.csv' -exec bash -c 'Rscript labels-per-image-hist.r `dirname {}`' \;
    find . -name 'labels_1_3.csv' -exec ./extract-csv-columns.sh {} 1 \;
    for i in 3 4; do
        find . -name "labels_$i.csv" -exec ./wordcount.py {} \;
    done
fi