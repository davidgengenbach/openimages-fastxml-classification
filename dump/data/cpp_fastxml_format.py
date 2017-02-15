#!/usr/bin/env python3
"""
Takes the features-classes file and splits them into two files. For C++ fastxml

Input:
    d9103825a5288a15,-4.47296,...,3.31911 /m/01280g,...,/m/0jly1
Output:
    classes
    features
"""

import argparse
import numpy as np
import pickle
import time
import os
import subprocess

DEFAULT_IN_FEATURES_WITH_CLASSES = 'out/features.labels.txt'
DEFAULT_OUT_FEATURES_FORMAT_CPP = 'out/cpp.fastxml.features.txt'
DEFAULT_OUT_CLASSES_FORMAT_CPP = 'out/cpp.fastxml.classes.txt'
DEFAULT_IN_CLASSES_SORTED = 'data/classes.sorted.txt'


def main():
    parser = argparse.ArgumentParser(description='Format features with classes to py-fastxml format')
    parser.add_argument('--features-labels-file', type=str, help="IN", default=DEFAULT_IN_FEATURES_WITH_CLASSES)
    parser.add_argument('--classes-sorted-file', type=str, help="IN classes sorted",
                        default=DEFAULT_IN_CLASSES_SORTED)
    parser.add_argument('--features-out-file', type=str, help="OUT features", default=DEFAULT_OUT_FEATURES_FORMAT_CPP)
    parser.add_argument('--classes-out-file', type=str, help="OUT classes", default=DEFAULT_OUT_CLASSES_FORMAT_CPP)
    args = parser.parse_args()

    features_and_classes = get_features_and_classes(args.features_labels_file)
    feature_count = get_feature_count(args.features_labels_file)
    features_count = get_file_line_count(args.features_labels_file)

    classes_ = open(args.classes_sorted_file).read().split('\n')
    classes_.sort()

    write(args.features_out_file, args.classes_out_file, features_and_classes, classes_, feature_count, features_count)


def write(features_out_file, classes_out_file, features_and_classes, classes_, feature_count, features_count):
    features_indexes = range(feature_count)

    with open(features_out_file, 'w') as feature_file:
        feature_file.write('{} {}\n'.format(features_count, feature_count))
        with open(classes_out_file, 'w') as classes_file:
            classes_file.write('{} {}\n'.format(features_count, len(classes_)))
            for line in features_and_classes:
                line = line.strip()
                if line == '':
                    continue
                if line.count(' ') != 1:
                    print("Invalid features/classes line: {}".format(line))
                    continue
                features, classes = line.split(' ')
                iid = features[0:16]
                features = features[17:].split(',')
                classes = classes.split(',')

                # Features
                feature_file.write(" ".join(['{}:{}'.format(idx, feature)
                                             for idx, feature in zip(features_indexes, features)]))
                feature_file.write('\n')

                for clazz in classes:
                    if clazz not in classes_:
                        print("Class not found: {}".format(clazz))

                # Classes
                classes_file.write(' '.join(['{}:1'.format(classes_.index(clazz)) for clazz in classes]))
                classes_file.write('\n')


def get_feature_count(file):
    with open(file) as f:
        count = 0
        while count == 0:
            count = f.readline().split(' ')[0].count(',')
    return count


def get_file_line_count(file):
    p = subprocess.Popen(['wc', '-l', file], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])


def get_features_and_classes(file):
    with open(file) as f:
        for line in f:
            yield line

if __name__ == '__main__':
    main()
