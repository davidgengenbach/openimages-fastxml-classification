#!/usr/bin/env python

from glob import glob
import numpy as np

results = glob('*_results.txt')
#results = ['openimages__NUM_THREADS__3__START_TREE__0__NUM_TREE__5__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__10__LBL_PER_LEAF__1_train_results.txt', 'openimages__NUM_THREADS__2__START_TREE__0__NUM_TREE__10__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__20__LBL_PER_LEAF__10_train_results.txt', 'openimages__NUM_THREADS__3__START_TREE__0__NUM_TREE__5__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__10__LBL_PER_LEAF__1_test_results.txt', 'openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_test_results.txt', 'openimages__NUM_THREADS__2__START_TREE__0__NUM_TREE__10__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__20__LBL_PER_LEAF__10_test_results.txt', 'openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_train_results.txt', 'openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__30__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_results.txt', 'openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__20__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_results.txt']

def get_parameters_from_filename(filename):
    parts = filename.split('__')
    assert(len(parts) == 12)
    parts[-1] = parts[-1].split('_')[0]
    key = None
    params = {}
    for idx, part in enumerate(parts):
        if idx % 2 == 0:
            key = part
        else:
            if key == 'NUM_THREADS':
                continue
            params[key] = part
    return params

results = sorted([get_parameters_from_filename(x) for x in results], key = lambda x: int(x['NUM_TREE']))
print(" ".join(results[0].keys()))
for result in results:
    print(" ".join(["{:5}".format(str(x)) for x in result.values()]))
