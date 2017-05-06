#!/usr/bin/env python
'''
Prints labels with probabilities of each datapoint in FastXML results file.
'''

import argparse
import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description='desc')
    parser.add_argument('--results-file', type=str, help="help")
    parser.add_argument('--classes-file', type=str, help="help", default='reference/classes.sorted.txt')
    parser.add_argument('--labels-map', type=str, help="help", default='reference/dict.csv')
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    label_map = get_label_map(args.labels_map)
    labels_sorted = get_sorted_labels(args.classes_file)

    with open(args.results_file) as f:
        results = f.read().split('\n')
    items = [parse_result(x) for x in results[1:] if x.strip() != '']
    for idx, item in enumerate(items):
        item = sorted(item, reverse=True, key=lambda x: x[1])
        print('Image: {}'.format(idx))
        print_labels(item, label_map, labels_sorted)


def print_labels(item, label_map, labels_sorted, threshold_prob=0.05):
    for label_idx, label_prob in item:
        if label_prob < threshold_prob:
            continue
        label_id = labels_sorted[label_idx]
        label_name = label_map[label_id]
        print('{:.2f}\t{:<20}'.format(label_prob, label_name))


def parse_result(result):
    labels = [(int(x.split(':')[0]), float(x.split(':')[1])) for x in result.split(' ') if x.strip() != '']
    return labels


def get_sorted_labels(classes_file):
    with open(classes_file) as f:
        return [x.strip() for x in f.read().split('\n') if x.strip() != '']


def get_label_map(labelmap_file):
    labels = {}
    with open(labelmap_file) as f:
        for x in f.read().split('\n'):
            parts = x.split(',')
            if len(parts) < 2:
                continue
            label_id = parts[0].replace('"', '')
            label_name = parts[1].replace('"', '')
            labels[label_id] = label_name
    return labels


if __name__ == '__main__':
    main()
