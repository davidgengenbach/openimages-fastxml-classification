#!/usr/bin/env python3
'''
Splits a file according to indices

Input: 
    Multiple files (= the sets) with the instance indices
Output:
    Multiple files (= the same number as in the input)
'''

import numpy as np
import math


def main():
    import os
    import pickle
    import functools
    import json
    args = get_args()

    with open(args.input_sets_file) as f:
        sets = json.load(f)

    out_files = [open('{}/{}.txt'.format(args.out_folder, set_idx), 'w') for set_idx in range(len(sets))]

    file_idxs = {idx: vals for idx, vals in enumerate(sets)}
    file_idxs_inverted = [-1] * sum([len(x) for x in sets])
    for key, val in file_idxs.items():
        for v in val:
            file_idxs_inverted[v] = key

    for val in file_idxs_inverted:
        assert(val >= 0)

    with open(args.input_file) as f:
        if not args.dont_skip_header:
            next(f)
        for target_idx, line in zip(file_idxs_inverted, f):
            out_files[target_idx].write(line)

    for file in out_files:
        f.close()

def get_lines_of_file(file, strip_empty=True):
    with open(file) as f:
        return [x.strip() for x in f if not strip_empty or x.strip() != '']


def get_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Merge sets according to set file')
    parser.add_argument('--input_sets_file', type=str, default='out/sets.json')
    parser.add_argument('--input_file', type=str, default='in/cpp.fastxml.classes.txt')
    parser.add_argument('--dont_skip_header', action='store_true')
    parser.add_argument('--out_folder', type=str, default='out/')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
