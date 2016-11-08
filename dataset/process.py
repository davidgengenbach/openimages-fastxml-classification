#!/usr/bin/env python
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import sys

if len(sys.argv) == 2:
    FILE_CSV = sys.argv[1]
else:
    FILE_CSV = 'labels.csv'

def get_header_index_from_name(name, headers):
    for idx, header in enumerate(headers):
        if name == header:
            return idx
    return None

line_count = int(os.popen('wc -l < {}'.format(FILE_CSV)).read().strip())

DICT = {}
with open(FILE_CSV) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(csv_reader)
    image_id_header = get_header_index_from_name('ImageID', headers)
    label_header = get_header_index_from_name('LabelName', headers)
    confidence_header = get_header_index_from_name('Confidence', headers)
    current_id = None
    for idx, row in enumerate(csv_reader):
        image_id = row[image_id_header]
        if current_id != image_id:
            assert(image_id not in DICT)
            DICT[image_id] = []
            current_id = image_id
        label = row[label_header]
        if float(row[confidence_header]) != 0:
            DICT[image_id].append(label)
        if idx == 100000:
            pass
        if round((idx / line_count) * 100 % 10, 4) == 0 and idx != 0:
            print("{:<2}%".format(int((idx / line_count) * 100)))

print("Finished counting")

label_count_only = [len(val) for val in DICT.values()]
bins = {}
for label_count in label_count_only:
    if label_count not in bins:
        bins[label_count] = 0
    bins[label_count] += 1
image_count = sum(bins.values())
rel_bins = {k: v / image_count for k, v in bins.items()}

assert(round(sum(rel_bins.values()), 4) == 1)

def print_bins(bins, filename, dpi = 200):
    fig = plt.figure(figsize = (16, 4))
    plt.bar(range(len(bins)), bins.values(), align='center')
    plt.xticks(range(len(bins)), bins.keys())
    plt.savefig(filename, dpi = dpi)

print_bins(rel_bins, 'yes.png')
