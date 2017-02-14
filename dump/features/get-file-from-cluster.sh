#!/usr/bin/env bash

FILE=$1
PREFIX='ke:/nfs/home/dgengenbach/cluster_files/feature_extraction'

rsync -P "$PREFIX/$FILE" .
