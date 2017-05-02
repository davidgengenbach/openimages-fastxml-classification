#!/usr/bin/env bash

IN=$1
OUT=$2
MODEL="openimages"


INSTALL_DEPS=1
SETUP=1

if [ "$IN" == "" ]; then
    IN='data/in.txt'
fi

if [ "$OUT" == "" ]; then
    OUT='data/out.txt'
fi

if [ "$INSTALL_DEPS" == 1 ]; then
 pip3 install -r requirements.txt
fi

if [ "$SETUP" == 1 ]; then
    python3 setup.py install
fi

fxml.py $MODEL $IN \
        --standard-dataset \
        --verbose \
        train \
        --iters 1 \
        --threads 2 \
        --trees 20 \
        --label-weight propensity \
        --alpha 1e-4 \
        --leaf-classifiers \
        --no-remap-labels

fxml.py $MODEL $OUT \
        --standard-dataset \
        --verbose \
        inference \
        --score