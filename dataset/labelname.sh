#!/usr/bin/env bash

LABEL_ID=$1

cat download/dict.csv | grep $LABEL_ID | cut -d , -f 2 | tr -d '"'