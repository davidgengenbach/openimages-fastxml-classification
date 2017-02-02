#!/usr/bin/env bash

REMOTE=/nfs/cluster_files/dgengenbach/feature_extraction/tensorflow-vgg

rsync -avP --exclude __pycache__ . ke:$REMOTE

