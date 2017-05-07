#!/usr/bin/env bash

TENSORFLOW_VGG_PATH="/nfs/cluster_files/dgengenbach/ml-praktikum/vgg/tensorflow-vgg"
DATA_PATH="/nfs/cluster_files/dgengenbach/ml-praktikum/data"

FEATURE_TO_EXTRACT=$1

if [ -z "$FEATURE_TO_EXTRACT" ]; then
    echo "Usage: $0 feature_layer_to_extract"
    exit 1
fi

cd $TENSORFLOW_VGG_PATH

python3 test_vgg16.py \
    --images-list-file $DATA_PATH/images.txt \
    --images-path $DATA_PATH/val_imgs/ \
    --done-file $DATA_PATH/done.$FEATURE_TO_EXTRACT.txt \
    --features-file $DATA_PATH/features.$FEATURE_TO_EXTRACT.txt \
    --batch-size 1 \
    --extract-layers $FEATURE_TO_EXTRACT