#!/usr/bin/env python
import sys
import helper
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "text.fontsize": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    #"figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
    ]
}
mpl.rcParams.update(pgf_with_latex)


mpl.use('pgf')
# seaborn.set_style("whitegrid")
sns.set_style("whitegrid", {'axes.grid': False})
import numpy as np

DIR_IN = sys.argv[1]
FILE_IN = "{}/labels_per_image.csv".format(DIR_IN)
PLOT_OUT = "{}/labels_per_image.pgf".format(DIR_IN)

INPUT = open(FILE_IN)
next(INPUT)  # Skip header
line_count = helper.get_line_count(FILE_IN) - 1
helper.print_file_count(FILE_IN, line_count)


def get_xy_data(d):
    return list(map(int, d.strip().split(',')))


def plot_labels_per_image(data, filename, dpi=300, figsize=(6, 3)):
    assert(len(data[:, 0]) == len(data[:, 1]))


    fig = plt.figure(figsize=figsize, frameon = False)
    ax = plt.gca()
    # print()
    plt.bar(data[:, 0], data[:, 1] / sum(data[:, 1]) * 100, align='center', color='#F5A238')

    #for spine in plt.gca().spines.values():
    #    spine.set_visible(False)
    #plt.axes.Axes.set_xlabel(xlabel = 'yes')
    ax.set_xlabel('\# Annotations')
    ax.set_ylabel('\%')

    plt.tight_layout()
    plt.savefig(filename, dpi=dpi, bbox_inches='tight')

data = np.array([get_xy_data(x) for x in INPUT], dtype=np.int32)
plot_labels_per_image(data, PLOT_OUT)
'''
a = 0
sum_images = sum([images for labels, images in data])
for labels, images in data:
    a += labels * images
print(a / sum_images)
minimum = min([labels for labels, images in data if images > 0])
maximum = max([labels for labels, images in data if images > 0])
print(minimum, maximum)
print([images for labels, images in data if labels == 36])
'''
