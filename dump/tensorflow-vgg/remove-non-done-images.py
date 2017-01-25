#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Remove non-done images')
parser.add_argument('--done-file', default='done.txt')
parser.add_argument('--features-file', default='features.txt')
args = parser.parse_args()

done = set(open(args.done_file).read().split('\n'))
features = set(open(args.features_file).read().split('\n'))

real_done = done.intersection(features)
print(len(done), len(features), len(real_done))