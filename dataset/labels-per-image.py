#!/usr/bin/env python
import sys
import helper
import matplotlib.pyplot as plt
import seaborn
import numpy as np

DIR_IN = sys.argv[1]
FILE_IN="{}/labels_per_image.csv".format(DIR_IN)
PLOT_OUT="{}/labels_per_image.png".format(DIR_IN)


INPUT = open(FILE_IN)
next(INPUT) # Skip header
line_count = helper.get_line_count(FILE_IN) - 1
helper.print_file_count(FILE_IN, line_count)

def get_xy_data(d):
    return list(map(int, d.strip().split(',')))

def plot_labels_per_image(data, filename, dpi = 200, figsize=(16,4)):
    assert(len(data[:,0]) == len(data[:,1]))
    fig = plt.figure(figsize = figsize)
    plt.bar(data[:,0], data[:,1], align='center')
    plt.savefig(filename, dpi = dpi)

data = np.array([get_xy_data(x) for x in INPUT], dtype=np.int32)

plot_labels_per_image(data, PLOT_OUT)

