#!/usr/bin/env bash

FEATURES_FILE="../features.txt"
FEATURES_LABELS_FILE="out/features_with_labels.txt"

./add-labels-to-features.py \
    --features-file $FEATURES_FILE  \
    --features-labels-file $FEATURES_LABELS_FILE \
    --labels 'data/labels_1_3_correct.sorted.csv' \
    --labels-npy 'data/labels_1_3_correct.npy'
