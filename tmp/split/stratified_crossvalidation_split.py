#!/usr/bin/env python3
'''
Implements the stratified k-fold cross-validation split algorithm.
For more info, see http://lpis.csd.auth.gr/publications/sechidis-ecmlpkdd-2011.pdf

TODO: See http://leo.ugr.es/MD-PGMs/ficheros_presentaciones/albacete3/SCVMLCGA.pdf

Input: 
    A file in sparse class format. Each line represents a instance. Each string before ":" on that line is a class.
    120:1 430:1
    ...
    123:1 99:1 10:1
Output:
    Mulitple files. TODO 
    1 4 2
'''

import numpy as np
import math
from time import time


def stratified_cross_validation_split(instances, k=10, r=None):
    """Creates a stratified cross-validation split of the given dataset as described in [1,2].

    [1] http://lpis.csd.auth.gr/publications/sechidis-ecmlpkdd-2011.pdf
    [2] https://de.slideshare.net/tsoumakas/on-the-stratification-of-multilabel-data

    Args:
        instances (list): Is a list of lists. For example [[1, 2, 3], [4,5]] means that the first instance has labels [1,2,3] attached, and the second item has the labels [4,5].
        k (int, optional): The number of folds
        r (None, optional): Weighting of sets. See paper

    Returns:
        list: A list with k lists. The items in one of the k lists are the indices of the instances. So when the list [[1, 3], [2,5]] is returned, the first set has the items [1, 3] and the second set has [2, 5] as instances. The number in the set are the indices of the instance in the "instances" parameter.
    """
    labels = get_all_labels(instances)

    num_labels = len(labels)
    num_instances = len(instances)

    assert(num_labels > 0)
    assert(num_instances > 0)
    assert(k > 0 and k <= num_instances)

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
    print("StratifyIterations: {}".format(counter + 1))
    return S


def main():
    import os
    import functools
    import json
    args = get_args()

    input_file = get_lines_of_file(args.input_file)
    if not args.dont_skip_header:
        input_file = input_file[1:]
    instances = [parse_line(x) for x in input_file]

    sets = stratified_cross_validation_split(instances, k=args.k)
    all_instances = functools.reduce(lambda acc, x: acc + x, sets, [])

    # Check that no duplicates are here
    assert(len(all_instances) == len(set(all_instances)))

    # Check that all instances are in a set (= no missing instances in splitted sets)
    assert(sum([len(x) for x in sets]) == len(instances))

    with open(args.out_file, 'w') as f:
        json.dump(sets, f, indent=4)


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
        description='Create stratified k-fold cross-validation sets')
    parser.add_argument('--input_file', type=str, default='cpp.fastxml.classes.txt')
    parser.add_argument('--out_file', type=str, default='out/sets.json')
    parser.add_argument('--dont_skip_header', action='store_true')
    parser.add_argument('--k', type=int, default=10)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
