#!/usr/bin/env sh

LABEL_PATH=$1
cat $LABEL_PATH/labels.csv | grep -o "...$" > $LABEL_PATH/only_conf.txt