#!/usr/bin/env python
"""
Takes the features and adds the labels to them.

Input:
    d9103825a5288a15,-4.47296,...,3.31911
Output:
    d9103825a5288a15,-4.47296,...,3.31911 /m/01280g,...,/m/0jly1
"""

import argparse
import numpy as np
import pickle
import time
import os


DEFAULT_IN_FEATURES_FILE = 'in/features.txt'
DEFAULT_LABELS_FILE = 'data/labels_1_3_correct.sorted.csv'
DEFAULT_LABELS_FILE_NPY = 'data/labels_1_3_correct.pickle'
DEFAULT_OUT_FEATURES_WITH_CLASSES = 'out/out.txt'

def main():
    parser = argparse.ArgumentParser(description='Adds labels to features')
    parser.add_argument('--features-file', type=str, help="IN", default=DEFAULT_IN_FEATURES_FILE)
    parser.add_argument('--features-labels-file', type=str, help="OUT", default=DEFAULT_OUT_FEATURES_WITH_CLASSES)
    parser.add_argument('--label-reprocess', action='store_true', help="reprocessing labels to npy", default=True)
    parser.add_argument('--labels', type=str, help="labels for the images: iid,label", default=DEFAULT_LABELS_FILE)
    parser.add_argument('--labels-npy', type=str, help="labels for the images as npy", default=DEFAULT_LABELS_FILE_NPY)
    args = parser.parse_args()

    labels = get_labels(args.labels, args.labels_npy, args.label_reprocess)
    features = get_features(args.features_file)
    write_features_with_labels_file(args.features_labels_file, labels, features)


def get_features(features_file):
    with open(features_file, 'r') as f:
        for line in f:
            yield line
        #return f.read().split('\n')

def write_features_with_labels_file(features_labels_file, labels, features):
    with open(features_labels_file, 'w') as outfile:
        for feature in features:
            iid = feature[0:16]
            if iid not in labels:
                continue
            labels_for_iid = labels[iid]
            outfile.write(feature + ' ' + ','.join(labels_for_iid))
            outfile.write('\n')


def get_labels(labels, labels_npy, process = False):
    if process and os.path.exists(labels_npy):
        with open(labels_npy, 'rb') as f:
            return pickle.load(f)
    else:
        with open(labels) as f:
            images_labels = [x.strip() for x in f.read().split() if x.strip() != '']
        l = {}
        for label in images_labels:
            if label.count(',') == 2 and label.endswith(',0.0'):
                label = label.replace(',0.0', '')
            if label.count(',') != 1:
                print("Invalid line: '{}'".format(label))
                continue
            iid, label = label.split(',')
            if iid not in l:
                l[iid] = []
            l[iid].append(label)
        with open(labels_npy, 'wb') as f:
            pickle.dump(l, f)
        return l


if __name__ == '__main__':
    main()
