#!/usr/bin/env bash

HERE=$(pwd)

test_features_file="$1"
score_file_test="$2"
model_dir="/Users/davidgengenbach/Documents/Projekte/ml-praktikum/dump/model
"
num_threads=4

usage() {
    echo "Usage: $0 in_features out_classes"
    exit 1
}

if ([ -z "$test_features_file" ] || [ -z "$score_file_test" ]); then
    usage
fi

test_features_file="$(pwd)/$test_features_file"
score_file_test="$(pwd)/$score_file_test"

cd cpp-FastXML_PfastreXML/FastXML
./fastXML_test \
        $test_features_file \
        $score_file_test \
        $model_dir \
        -T $num_threads