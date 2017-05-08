#!/usr/bin/env python3

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Split features')
    parser.add_argument('--in-file', type=str, default='data/features.fc7.fc8.small.txt')
    parser.add_argument('--split-points', type=str, default='4096,8192')
    parser.add_argument('--out_folder', type=str, default='data/splits')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    in_file = open(args.in_file)

    split_points = [int(x) for x in args.split_points.split(',')]
    files = [open('{}/split.{}.txt'.format(args.out_folder, x), 'w') for x in range(len(split_points) + 1)]
    comma_count = None
    for line in in_file:
        if line.strip() == '':
            continue
        if not comma_count:
            comma_count = line.count(',')
            split_points.append(comma_count)
        parts = line.split(',')
        iid = parts[0]
        for idx, split_point in enumerate(split_points):
            last = 0 if idx == 0 else split_points[idx - 1]
            part = parts[last + 1:split_point + 1]
            files[idx].write(','.join([iid] + part).strip() + '\n')

    for file in files:
        file.close()

if __name__ == '__main__':
    main()
