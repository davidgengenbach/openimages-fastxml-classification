#!/usr/bin/env bash

cleanup ()
{
    exit 1
}

trap cleanup SIGINT SIGTERM

for i in {1..30}; do
    python3 get_fscore_averaged.py
done