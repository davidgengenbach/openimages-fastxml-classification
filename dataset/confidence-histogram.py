#!/usr/bin/env python
import sys
import numpy as np
import helper
import time

FILE_IN = sys.argv[1]
NUM_BINS = 11

line_count = helper.get_line_count(FILE_IN) - 1
print('Lines: {}'.format(line_count))

bins = np.zeros(NUM_BINS, dtype=np.int32)
histogramm = np.zeros(NUM_BINS, dtype=np.int64)
percentage_points = [int(line_count * x) for x in np.arange(0.0, 1.1, 0.1)]

with open(FILE_IN) as f:
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
assert(bin_item_count== line_count + 1)

print("\n{}".format(FILE_IN))
for idx, b in enumerate(bins):
    #print("{:.1f} -> {}".format(idx / 10, b))
    print("{:.1f} -> {:>4.1f}%".format(idx / 10, b / bin_item_count * 100))
