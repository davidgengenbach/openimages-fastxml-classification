#!/usr/bin/env python3

import argparse

def main():
    args = get_args()
    in_file = open(args.in_file)
    out_file_1 = open(args.out_1_file, 'w')
    out_file_2 = open(args.out_2_file, 'w')

    if args.ignore_header:
        header = next(in_file)

    out_file_1.write(header)
    out_file_2.write(header)

    count = 4096
    for line in in_file:
        if line.strip() == '':
            continue
        comma_count = line.count(',')
        parts = line.split(',', count + 1)
        assert(len(parts) == count + 2)
        iid = parts[0]
        part_1 = parts[1:-1]
        assert(len(part_1) == count)
        assert(parts[-1].count(',') == 1000 - 1)
        out_file_1.write(",".join([iid] + part_1) + '\n')
        out_file_2.write(iid + ',' + parts[-1] + '\n')

    out_file_1.close()
    out_file_2.close()

def get_args():
    parser = argparse.ArgumentParser(description='Split features')
    parser.add_argument('--in-file', type=str, default='data/features.fc7.fc8.small.txt')
    parser.add_argument('--ignore-header', default=False, action='store_true')
    parser.add_argument('--out-1-file', type=str, default='data/features.fc7.txt')
    parser.add_argument('--out-2-file', type=str, default='data/features.fc8.txt')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()