#!/usr/bin/env python3
'''
Input: 
    Classes:
        158208 7881
        51:1 52:1 224:1 1221:1 1223:1 3181:1 7454:1 7537:1 7553:1
    Features:
        1 5096
        0:2.14914 1:-2.67836 .... 5094:1.52956
Output:
    ???
'''

import argparse

DEFAULT_IN_CLASSES_SPARSE = 'in/classes.real.txt'
DEFAULT_IN_FEATURES_SPARSE = '../features.txt'
DEFAULT_OUT = 'out/yes.txt'
NUM_FEATURES = 5096
NUM_CLASSES = 7881

def main():
    parser = argparse.ArgumentParser(description='Converts to MULAN formats')
    parser.add_argument('--classes-in-file', type=str, default=DEFAULT_IN_CLASSES_SPARSE)
    parser.add_argument('--features-in-file', type=str, default=DEFAULT_IN_FEATURES_SPARSE)
    parser.add_argument('--out-file', type=str, default=DEFAULT_OUT)
    parser.add_argument('--header', type=str, default=DEFAULT_OUT)
    args = parser.parse_args()

    header = get_header(NUM_FEATURES, NUM_CLASSES)

    clazzes = get_classes(args.classes_in_file)
    features = get_features(args.features_in_file)
    with open(args.out_file, 'w') as f:
        f.write(header)
        for clazzes, feature in zip(clazzes, features):
            features_ = ",".join([str(idx) + ' ' + str(x) for idx, x in enumerate(feature)])
            clazzes_ = ",".join([str(classid + NUM_FEATURES) + ' ' + str(val) for classid, val in clazzes])
            f.write('{{{},{}}}\n'.format(features_, clazzes_))


def get_header(NUM_FEATURES, NUM_CLASSES):
    out = ['@relation OpenImages', '']
    out += ['@attribute f%s numeric' % x for x in range(NUM_FEATURES)]
    out += ['@attribute c%s {0,1}' % x for x in range(NUM_CLASSES)]
    return '\n'.join(out)

def get_features(file):
    with open(file) as f:
        for feature_line in f:
            yield feature_line.split(',')[1:]

def get_classes(file):
    print("Getting: {}".format(file))
    elements = []
    with open(file) as f:
        num_elements, num_classes = f.readline().split(' ')
        elements = f.read().strip().split('\n')
        num_elements = len(elements)
        num_classes = int(num_classes)
    elements_out = []
    for idx, element in enumerate(elements):
        if element.strip() == '':
            print("Empty element: {}".format(idx))

        clazzes = []
        for clazz in element.split(' '):
            clazz_idx, val = clazz.split(':')
            clazz_idx = int(clazz_idx)
            val = float(val)
            if not val >= 0 or not val <= 1:
                print("Invalid val: {}".format(val))
            clazzes.append((clazz_idx, val))
        elements_out.append(clazzes)
    return elements_out

if __name__ == '__main__':
    main()