#!/usr/bin/env python3
'''
Implements the stratified k-fold cross-validation split algorithm.
See http://lpis.csd.auth.gr/publications/sechidis-ecmlpkdd-2011.pdf

Input: 
    A file in sparse class format. Each line represents a instance. Each string before ":" on that line is a class.
    120:1 430:1
    ...
    123:1 99:1 10:1
Output:
    Mulitple files. 
    1 4 1
'''

import numpy as np
import math
from time import time


def stratified_cross_validation_split(instances, k=10, r=None):
    labels = get_all_labels(instances)
    num_labels = len(labels)
    num_instances = len(instances)

    if not r:
        r = [1 / k] * k

    # Calculate the desired number of examples at each subset
    c_1 = [math.floor(num_instances * x) for x in r]
    c_2 = {}
    # Calculate the desired number of examples of each label at each subset
    def get_D(used_instances):
        D = {}
        for idx, instance in enumerate(instances):
            for label in instance:
                if label not in D:
                    D[label] = []
                D[label].append(idx)
        # for label in labels:
        #    # Find the examples of each label in the initial set
        #    D_2[label] = [idx for idx, x in enumerate(instances) if label in x and idx not in used_instances]
        return D

    # Most expensive
    D = get_D(set())
    for label, vals in D.items():
        c_2[label] = [len(vals) * x for x in r]

    used_instances = set()
    S = [[] for x in range(k)]
    counter = 0
    checkpoints = [x * num_instances / k for x in range(k)]
    print('Starting sorting elements into sets')
    while len(used_instances) < len(instances):
        if len(checkpoints) and len(used_instances) > checkpoints[0]:
            print('{:>2.0f}%'.format(len(used_instances) / len(instances) * 100))
            checkpoints = checkpoints[1:] if len(checkpoints) else []
        counter += 1
        # Find the label with the fewest (but at least one) remaining examples, breaking ties randomly
        def sort_fn(x):
            return len(x[1])
        l = min(D.items(), key=sort_fn)
        l = l[0]
        for inst in D[l]:
            M = sorted(enumerate(c_2[l]), key=lambda x: x[1])
            M = [(idx, examples_wished) for idx, examples_wished in M if examples_wished == M[-1][1]]
            if len(M) == 1:
                m = M[0][0]
            else:
                idxs = [x[0] for x in M]
                np.random.shuffle(idxs)
                s = sorted([(idx, x) for idx, x in enumerate(c_1) if idx in idxs], key=lambda x: [1])
                s = [idx for idx, x in s if x == s[-1][1]]
                if len(s) == 1:
                    m = s[0]
                else:
                    m = s[np.random.randint(0, len(s))]
            # Find the subset(s) with the largest number of desired examples for this
            # label, breaking ties by considering the largest number of desired
            # examples, breaking further ties randomly
            Y = instances[inst]
            S[m].append(inst)
            used_instances.add(inst)
            # Update desired number of examples
            for label in Y:
                if inst in D[label]:
                    # Instead of updating D globally on each iteration, update it on each instance
                    D[label].remove(inst)
                    if len(D[label]) == 0:
                        # Delete label from D so that the sorting gets faster
                        del D[label]
                c_2[label][m] -= 1
            c_1[m] -= 1
    print("StratifyIterations needed: {}".format(counter + 1))
    return S


def main():
    import os
    import pickle
    import functools
    args = get_args()

    pickle_filename = args.input_file + '.pickle'
    if os.path.exists(pickle_filename):
        with open(pickle_filename, 'rb') as f:
            instances = pickle.load(f)
    else:
        input_file = get_lines_of_file(args.input_file)
        if not args.dont_skip_header:
            input_file = input_file[1:]
        instances = [parse_line(x) for x in input_file]
        with open(pickle_filename, 'wb') as f:
            pickle.dump(instances, f)

    sets = stratified_cross_validation_split(instances, k=args.k)
    all_instances = functools.reduce(lambda acc, x: acc + x, sets, [])

    # Check that no duplicates are here
    assert(len(all_instances) == len(set(all_instances)))

    # Check that all instances are in a set (= no missing instances in splitted sets)
    assert(sum([len(x) for x in sets]) == len(instances))

    for idx, elements in enumerate(sets):
        print('Set {}: {}'.format(idx, len(elements)))
        set_filename = '{}/set.{}.{}.txt'.format(args.out_folder, idx, args.input_file.replace('/', '__'))
        with open(set_filename, 'w') as f:
            f.write(" ".join(sorted([str(x) for x in elements])))


def get_all_labels(instances):
    all_labels = set()
    for x in instances:
        all_labels |= set(x)
    return all_labels


def parse_line(line):
    return set([int(x.split(':')[0]) for x in line.split(' ')])


def get_lines_of_file(file, strip_empty=True):
    with open(file) as f:
        return [x.strip() for x in f if not strip_empty or x.strip() != '']


def get_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Create a stratified cross-validation see (see http://lpis.csd.auth.gr/publications/sechidis-ecmlpkdd-2011.pdf)')
    parser.add_argument('--input_file', type=str, default='cpp.fastxml.classes.txt')
    parser.add_argument('--out_folder', type=str, default='out/')
    parser.add_argument('--dont_skip_header', action='store_true')
    parser.add_argument('--k', type=int, default=10)
    args = parser.parse_args()
    args.out_folder = args.out_folder[0:-1] if args.out_folder.endswith('/') else args.out_folder
    return args

if __name__ == '__main__':
    main()
