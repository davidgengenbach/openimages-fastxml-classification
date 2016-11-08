#!/usr/bin/env python
import sys
import numpy as np
import helper
import sys
import time

MODE = sys.argv[1]
if MODE == "-":
    INPUT = sys.stdin
    OUTPUT = sys.stdout
    print_process_fn = None
else:
    FILE_IN = sys.argv[1]
    FILE_OUT = FILE_IN.replace('.csv', '_wc.txt')
    INPUT = open(FILE_IN)
    OUTPUT = open(FILE_OUT, 'w')
    line_count = helper.get_line_count(FILE_IN) - 1
    print('File:\t{}\nLines:\t{}\n'.format(FILE_IN, line_count))
    print_process_fn = helper.get_print_process_fn(line_count)

vals = {}
next(INPUT)
for idx, conf in enumerate(INPUT):
    if print_process_fn is not None:
        print_process_fn(idx)
    conf = conf.strip()
    if conf not in vals:
        vals[conf] = 0
    vals[conf] += 1

vals = list(vals.items())
vals.sort(key = lambda x: x[1], reverse = True)
OUTPUT.write('"word","count"\n')
OUTPUT.write("\n".join(["{},{}".format(k, v) for k, v in vals]))
OUTPUT.write('\n')
OUTPUT.flush()

OUTPUT.close()
INPUT.close()