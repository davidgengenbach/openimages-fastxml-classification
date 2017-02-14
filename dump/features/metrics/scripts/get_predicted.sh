#!/usr/bin/env bash

rsync -aP \
    ke:/nfs/home/dgengenbach/cluster_files/fast_xml/results/*.txt \
    in/
