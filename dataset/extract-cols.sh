#!/usr/bin/env bash

extract_columns() {
    echo -e "\tExtracting column: $1\t// $2 // $3"
    local COLUMNS=$1; local IN=$2; local OUT=$3;
    if [ -e "$OUT" ]; then
        echo -e "\t(Already extracted - skipping)"
    else
        csvtool col $COLUMNS $IN > $OUT
    fi

}

extract_ann_cols() {
    local IN=$1
    echo -e "\n\nextract_ann_cols: $IN"

    extract_columns 1,3 $IN/labels.csv      $IN/labels_1_3.csv || exit
    extract_columns 1   $IN/labels_1_3.csv  $IN/labels_1.csv || exit
    extract_columns 2   $IN/labels_1_3.csv  $IN/labels_3.csv || exit
    extract_columns 4   $IN/labels.csv      $IN/labels_4.csv || exit

    echo -e "\n\tStarting to count"
    ./wordcount.py $IN/labels_1.csv > /dev/null|| exit
    ./wordcount.py $IN/labels_3.csv > /dev/null || exit
    ./wordcount.py $IN/labels_4.csv > /dev/null || exit

    echo -e "\n\tLabels per image"
    ./labels-per-image.sh $IN
}

extract_img_cols() {
    local IN=$1
    echo -e "\n\nextract_img_cols: $IN"
    extract_columns 1,3,4   $IN/images.csv          $IN/images_1_3_4.csv || exit
    extract_columns 1,2     $IN/images_1_3_4.csv    $IN/images_1_3.csv || exit
    extract_columns 9       $IN/images.csv          $IN/images_9.csv || exit
}

extract_ann_cols "download/human_ann_2016_08/validation"
extract_ann_cols "download/machine_ann_2016_08/validation"
extract_ann_cols "download/machine_ann_2016_08/train"

echo -e "\n\nlabels-mispredicted"
./labels-mispredicted.sh

extract_img_cols "download/images_2016_08/validation"
extract_img_cols "download/images_2016_08/train"
