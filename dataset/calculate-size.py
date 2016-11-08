#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv

def load_csv(csv_filepath):
    with open(csv_filepath, 'r') as fp:
        reader = csv.reader(fp)
        next(reader)  # skip header
        lists = list(reader)
    return lists

CSVs = ['download/images_2016_08/train/images.csv', 'download/images_2016_08/validation/images.csv']

def get_header_index(name, headers):
    for idx, header in enumerate(headers):
        if header == name:
            return idx
    return None

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

STEPS = 1000000
for c in CSVs:
    size = 0
    headers = []
    with open(c, 'r') as fp:
        reader = csv.reader(fp)
        headers = next(reader)
        size_header_index = get_header_index('OriginalSize', headers)
        for idx, row in enumerate(reader):
            size += int(row[size_header_index])
            if idx % STEPS == 0 and idx != 0:
                print('Step {}'.format(idx))
        print('\n\n{} -> {}'.format(c, sizeof_fmt(size)))