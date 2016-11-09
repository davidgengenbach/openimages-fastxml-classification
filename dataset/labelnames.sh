#!/usr/bin/env bash

OUT=""
while read x ; do
    label_name=$(./labelname.sh $x)
    if [ "$label_name" == "" ]; then
        label_name="(NOT FOUND)"
    fi

    OUT="${OUT}\n${x}_${label_name}"
done
echo -e $OUT | column -t -s_