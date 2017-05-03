#!/usr/bin/env python3

import argparse

PARAMS_KEY_ORDER = ['NUM_TREE', 'MAX_LEAF', 'LBL_PER_LEAF']

def main():
    args = get_args()
    metrics = get_metrics(args.in_file)
    metrics.sort(key = lambda x: (int(x[0]['NUM_TREE']), int(x[0]['MAX_LEAF']), int(x[0]['LBL_PER_LEAF'])))

    result = []
    for params, precision in metrics:
        out = []
        precision = "{:.3f}".format(precision)

        for key in PARAMS_KEY_ORDER:
            out.append(params[key])
        out.append(precision)
        table_row = " & ".join(out)
        result.append(table_row)
        print(precision)

    print(" \\\ \hline \n".join(result))

def get_args():
    parser = argparse.ArgumentParser(description='Create a latex metrics table')
    parser.add_argument('--out', type=str, help="help", default='latex_table.tex')
    parser.add_argument('--in-file', type=str, help="help", default='metrics.test.txt')
    args = parser.parse_args()
    return args

def get_parameters_from_filename(filename):
    filename = filename.split('/')[-1]
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

def get_lines_from_file(file, remove_empty = True, strip = True):
    with open(file) as f:
        return [x.strip() if strip else x for x in f.read().split('\n') if not remove_empty or x.strip() != '']

def get_metrics(filename):
    out = []
    lines = get_lines_from_file(filename)
    key = None
    for line in lines:
        if line.startswith('#'):
            key = get_parameters_from_filename(line.replace('#', ''))
        else:
            out.append((key, float(line.replace('Total Precision@5: ', ''))))
    return out

if __name__ == '__main__':
    main()