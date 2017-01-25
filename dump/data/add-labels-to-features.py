#!/usr/bin/env python

import numpy as np
import pickle

REPROCESS_LABELS = False

FEATURES_FILE = 'features.txt'
LABELS_FILE = 'labels_1_3_correct.sorted.csv'
LABELS_FILE_NPY = 'labels_1_3_correct.pickle'
OUT = 'out.txt'

def get_labels(process = False):
    if process:
        with open(LABELS_FILE) as f:
            labels = f.read().split()
        l = {}
        for label in labels:
            iid, label = label.split(',')
            if iid not in l:
                l[iid] = []
            l[iid].append(label)
        with open(LABELS_FILE_NPY, 'wb') as f:
            pickle.dump(l, f)
    else:
        with open(LABELS_FILE_NPY, 'rb') as f:
            l = pickle.load(f)
    return l

with open(FEATURES_FILE) as f:
    features = f.read().split()

import time

labels = get_labels()
out_file = open(OUT, 'w')
for feature in features:
    iid = feature[0:16]
    if iid not in labels:
        continue
    labels_for_iid = labels[iid]
    out_file.write(feature + ' ' + ','.join(labels_for_iid))
    out_file.write('\n')

out_file.close()
