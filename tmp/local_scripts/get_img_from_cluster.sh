#!/usr/bin/env bash

IMG="$1"
OPEN_AFTERWARDS="$2"

if [ -z "$IMG" ]; then
    echo "Usage: $0 img_name"
    exit 1
fi

SERVER='ke'
IMG_FOLDER='imgs/'
SEARCH_FOLDER='/nfs/cluster_files/dgengenbach/ml-praktikum/data'

IMG_PATH=$(ssh $SERVER "find $SEARCH_FOLDER -name '$IMG*'")

if [ -z "$IMG_PATH" ]; then
    echo "Image not found: '$IMG'"
    exit 1
fi

scp $SERVER:$IMG_PATH $IMG_FOLDER

if [ "$OPEN_AFTERWARDS" == 1 ]; then
    open $IMG_FOLDER/$(basename $IMG_PATH)
fi