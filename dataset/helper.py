import os
import matplotlib.pyplot as plt
import numpy as np

def get_line_count(filename):
    return int(os.popen('wc -l < {}'.format(filename)).read().strip()) - 1

def print_file_count(filename, line_count):
    print('File:\t{}\nLines:\t{}'.format(filename, line_count))

def get_header_index_from_name(name, headers):
    for idx, header in enumerate(headers):
        if name == header:
            return idx
    return None

def get_percent_points(line_count):
    return [int(line_count * x) for x in np.arange(0.0, 1.1, 0.1)]

def get_print_process_fn(line_count):
    percentage_points = get_percent_points(line_count)
    def print_fn(idx):
        if idx in percentage_points:
            percentage = percentage_points.index(idx)
            print("{}%".format(int((percentage) * 10)))
    return print_fn

def print_bins_dict(bins, filename, dpi = 200):
    print_bins_arr(bins, bins.keys(), dpi)

def print_bins_arr(bins, labels, filename, dpi = 200):
    assert(len(bins) == len(labels))
    fig = plt.figure(figsize = (16, 4))
    plt.bar(range(len(bins)), bins, align='center')
    plt.xticks(range(len(bins)), labels)
    plt.savefig(filename, dpi = dpi)