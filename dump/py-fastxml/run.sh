#!/usr/bin/env bash

IN=$1
OUT=$2
MODEL="openimages"

if [ "$IN" == "" ]; then
    IN='data/in.txt'
fi

if [ "$OUT" == "" ]; then
    OUT='data/out.txt'
fi

python setup.py install

fxml.py $MODEL $IN \
        train \
        --standard-dataset \
        --verbose \
        --iters 1 \
        --threads 4 \
        --trees 20 \
        --label-weight propensity \
        --alpha 1e-4 \
        --leaf-classifiers \
        --no-remap-labels

fxml.py $MODEL $OUT \
        inference \
        --standard-dataset \
         --score