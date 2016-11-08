#!/usr/bin/env bash

download_and_extract() {
    FILE=$1
    wget "https://storage.googleapis.com/openimages/2016_08/$FILE"
    tar xf $FILE && rm $FILE
}

export DOWNLOAD_DIR='./download'
if [ ! -d "$DOWNLOAD_DIR" ]; then
    mkdir ${DOWNLOAD_DIR}
fi
cd ${DOWNLOAD_DIR}

#download_and_extract "images_2016_08_v5.tar.gz"
download_and_extract "machine_ann_2016_08_v3.tar.gz"
download_and_extract "human_ann_2016_08_v3.tar.gz"

wget "https://raw.githubusercontent.com/openimages/dataset/master/dict.csv"