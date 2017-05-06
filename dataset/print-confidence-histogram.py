#!/usr/bin/env python
'''
Puts the confidences in bins and prints them.

Input:
    Confidence
    0.0
    1.0
    ...
Output:
    0.0     41%
    ...
    1.0     20%
'''

import sys
import numpy as np
import helper
import time
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Get histogramm of confidences')
    parser.add_argument('file_in', type=str, help="Only confidences from [0.0, ..., [1.0]")
    parser.add_argument('--num-bins', type=int, help="Number of bins", default = 10)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    confidence_file_in = args.file_in
    num_bins = args.num_bins + 1

    line_count = helper.get_line_count(confidence_file_in) - 1
    print('Lines: {}'.format(line_count))

    bins = np.zeros(num_bins, dtype=np.int32)
    histogramm = np.zeros(num_bins, dtype=np.int64)

    # [0.0, ..., 1.0]
    percentage_points = [int(line_count * x) for x in np.arange(0.0, 1.1, 0.1)]

    with open(confidence_file_in) as f:
        vals = np.zeros(line_count + 1, dtype=np.int32)
        next(f)
        for idx, conf in enumerate(f):
            if idx in percentage_points:
                percentage = percentage_points.index(idx)
                print("{}%".format(int((percentage) * 10)))
            vals[idx] = int(float(conf.strip()) * 10)
        vals = np.sort(vals)
        last = vals[0]
        count = 0
        for val in vals:
            if last != val and val:
                bins[last] = count
                count = 0
                last = val
            count += 1
        bins[last] = count

    bin_item_count = sum(bins)
    assert(bin_item_count == line_count + 1)

    print("\n" + confidence_file_in)
    for idx, b in enumerate(bins):
        print("{:.1f}\t\t{:>4.1f}%".format(idx / 10, b / bin_item_count * 100))


if __name__ == '__main__':
    main()
