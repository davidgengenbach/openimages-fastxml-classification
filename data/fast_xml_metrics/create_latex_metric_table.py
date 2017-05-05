#!/usr/bin/env python3

import argparse

PARAMS_KEY_ORDER = ['NUM_TREE', 'MAX_LEAF', 'LBL_PER_LEAF']

def main():
    args = get_args()
    metrics = get_metrics(args.in_file)
    s = [(params, val) for params, val in metrics.items()]
    
    s.sort(key = lambda x: (int(x[1]['params']['NUM_TREE']), int(x[1]['params']['MAX_LEAF']), int(x[1]['params']['LBL_PER_LEAF'])))
    result = []
    for params, vals in s:
        precision_test = "{:.3f}".format(vals['test'])
        precision_train = "{:.3f}".format(vals['train'])
        out = []

        for key in PARAMS_KEY_ORDER:
            out.append(vals['params'][key])
        out.append(precision_test)
        out.append(precision_train)
        table_row = " & ".join(out)
        result.append(table_row)

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
    out = {}
    lines = get_lines_from_file(filename)
    key = None
    for line in lines:
        line = line.split('/')[-1].replace('.txt', '')
        parts = line.split(' ')
        params_raw = parts[0]
        params_without_suffix = params_raw.replace('_test_results', '').replace('_train_results', '')
        params = get_parameters_from_filename(params_raw)
        val = float(parts[1])
        is_test = line.count('test_results') == 1
        if params_without_suffix not in out:
            out[params_without_suffix] = {'params':params}
        out[params_without_suffix]['test' if is_test else 'train'] = val
    return out

if __name__ == '__main__':
    main()