#!/usr/bin/env python

import os
from glob import glob 
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
file = sorted(glob(this_dir + '/' + 'features*.txt'))[-1]
with open(file) as f:
    lines = f.read().split('\n')

lines = [x + ' /g/11jy976z6' if x.count(',') > 0 and x.count('/') == 0 else x for x in lines if x.strip() != '']

with open(file, 'w') as f:
    f.write("\n".join(lines))