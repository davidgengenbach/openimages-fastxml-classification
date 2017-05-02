#!/usr/bin/env python3
'''
Input: 
158208 7881
51:1 52:1 224:1 1221:1 1223:1 3181:1 7454:1 7537:1 7553:1

Output:

'''

import argparse

DEFAULT_IN_SPARSE = 'in/classes.real.txt'
DEFAULT_OUT_SPARSE_MAT = 'out/classes.real.matlab.txt'


def get_args():
    parser = argparse.ArgumentParser(description='Adds labels to features')
    parser.add_argument('--in-file', type=str, default=DEFAULT_IN_SPARSE)
    parser.add_argument('--out-file', type=str, default=None)
    return parser.parse_args()


def main():
    args = get_args()

    data, rows, class_idxs = get_classes(args.in_file)
    out = get_matlab_sparse_format(data, rows, class_idxs)

    if args.out_file is None:
        args.out_file = '.'.join(args.in_file.split('.')[0:-1]) + '.mat.txt'

    with open(args.out_file, 'w') as f:
        f.write(out)


def get_matlab_sparse_format(data, rows, class_idxs):
    out = []
    for idx, data in enumerate(data):
        out.append(str(rows[idx] + 1) + ' ' + str(class_idxs[idx] + 1) + ' ' + str(data))
    return "\n".join(out)


def get_classes(file):
    print("Getting: {}".format(file))
    STEP = 10000
    elements = []
    with open(file) as f:
        num_elements, num_classes = f.readline().split(' ')
        elements = f.read().strip().split('\n')
        #elements = elements[0:10000]
        num_elements = len(elements)
        num_classes = int(num_classes)
    classes = []
    data = []
    class_idxs = []
    rows = []
    for idx, element in enumerate(elements):
        if idx % STEP == 0:
            print("\tElement: {:>14}/{}".format(idx, num_elements))

        if element.strip() == '':
            print("Empty element? {}".format(idx))

        clazzes = []
        for clazz in element.split(' '):
            clazz_idx, val = clazz.split(':')
            clazz_idx = int(clazz_idx)
            data.append(float(val))
            if not float(val) >= 0 or not float(val) <= 1:
                print("Invalid val: {}".format(float(val)))
            rows.append(idx)
            class_idxs.append(clazz_idx)
    return data, rows, class_idxs

if __name__ == '__main__':
    main()
