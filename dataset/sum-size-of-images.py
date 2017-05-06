#!/usr/bin/env python3
'''
Calculates the total size of all images in the dataset.
'''

import os
import csv

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

CSVs = ['download/images_2016_08/train/images_9.csv', 'download/images_2016_08/validation/images_9.csv']

for c in CSVs:
    size = 0
    with open(c, 'r') as reader:
        headers = next(reader)
        for idx, row in enumerate(reader):
            size += int(row.strip())
    print('{:<10} {}'.format(sizeof_fmt(size), c))