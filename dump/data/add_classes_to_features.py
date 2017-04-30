#!/usr/bin/env python3
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
import helper


DEFAULT_IN_FEATURES_FILE = 'in/features.txt'
DEFAULT_LABELS_FILE = 'data/labels_1_3_correct.sorted.csv'
DEFAULT_LABELS_FILE_NPY = 'data/labels_1_3_correct.pickle'
DEFAULT_OUT_FEATURES_WITH_CLASSES = 'out/features.labels.txt'

def main():
    parser = argparse.ArgumentParser(description='Adds labels to features')
    parser.add_argument('--features-file', type=str, help="IN", default=DEFAULT_IN_FEATURES_FILE)
    parser.add_argument('--features-labels-file', type=str, help="OUT", default=DEFAULT_OUT_FEATURES_WITH_CLASSES)
    parser.add_argument('--label-reprocess', action='store_true', help="reprocessing labels to npy", default=True)
    parser.add_argument('--labels', type=str, help="labels for the images: iid,label", default=DEFAULT_LABELS_FILE)
    parser.add_argument('--labels-npy', type=str, help="labels for the images as npy", default=DEFAULT_LABELS_FILE_NPY)
    args = parser.parse_args()

    labels = helper.get_labels(args.labels, args.labels_npy, args.label_reprocess)
    features = get_features(args.features_file)
    write_features_with_labels_file(args.features_labels_file, labels, features)


def get_features(features_file):
    with open(features_file, 'r') as f:
        for line in f:
            yield line

def write_features_with_labels_file(features_labels_file, labels, features):
    STEP_SIZE = 10000
    with open(features_labels_file, 'w') as outfile:
        for idx, feature in enumerate(features):
            # Print process
            if idx % STEP_SIZE == 0:
                print("Feature#: {}".format(idx))

            # ImageId
            iid = feature[0:16]
            if iid not in labels:
                print("ImageId has no positive labels: {}".format(iid))
                labels_for_iid = []
                # TODO UNCOMMENT! continue
            else:
                # The labels for this image
                labels_for_iid = labels[iid]

            
            

            # Format: iid,feature1,...,featureN label1,...,labelN
            outfile.write(feature.strip() + ' ' + ','.join(labels_for_iid))
            outfile.write('\n')


if __name__ == '__main__':
    main()
