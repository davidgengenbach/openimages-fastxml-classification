
import os
import matplotlib.pyplot as plt

def get_line_count(filename):
    return int(os.popen('wc -l < {}'.format(filename)).read().strip()) - 1

def get_header_index_from_name(name, headers):
    for idx, header in enumerate(headers):
        if name == header:
            return idx
    return None

def print_bins_dict(bins, filename, dpi = 200):
    print_bins_arr(bins, bins.keys(), dpi)

def print_bins_arr(bins, labels, filename, dpi = 200):
    assert(len(bins) == len(labels))
    fig = plt.figure(figsize = (16, 4))
    plt.bar(range(len(bins)), bins, align='center')
    plt.xticks(range(len(bins)), labels)
    plt.savefig(filename, dpi = dpi)