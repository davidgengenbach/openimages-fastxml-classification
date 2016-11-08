#!/usr/bin/env bash

while read x ; do
    echo -e "$x\t\t$(./labelname.sh $x)"
done