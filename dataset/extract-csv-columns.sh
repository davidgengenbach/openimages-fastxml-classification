#!/usr/bin/env bash


#set -x

IN=$1
HEADERS=$2
HEADERS_WITHOUT_SEP=`echo $HEADERS | tr , _`
OUT="${IN//.csv/_${HEADERS_WITHOUT_SEP}.csv}"

echo $IN

cat $IN | cut -d , -f $HEADERS > $OUT
head $OUT | sed -e 's/,,/, ,/g' | column -s, -t
