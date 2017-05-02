#!/usr/bin/env python
'''
Returns the parameters of a results file by parsing the filename.
'''

from glob import glob
import numpy as np

results = glob('*_results.txt')

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
