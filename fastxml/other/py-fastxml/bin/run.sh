#!/usr/bin/env bash

FOLDER="../data/Delicious"
PYTHONPATH='..:$PYTHONPATH' fxml.py delicious.model $FOLDER/deliciousLarge_train.txt --standard-dataset --verbose train --iters 5 --trees 20 --label-weight propensity --alpha 1e-4 --leaf-classifiers --no-remap-labels