#!/usr/bin/env python3

from glob import glob
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Test validicity of a feature set')
    parser.add_argument('feature_file_glob', type=str)
    parser.add_argument('--feature-size', type=int, default=5096)
    parser.add_argument('--step-size', type=int, default=10000)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    feature_files = glob(args.feature_file_glob)
    assert(len(feature_files) > 0)

    counter = 0
    for feature_file in feature_files:
        found_error = False
        with open(feature_file, 'r') as f:
            for idx, line in enumerate(f):
                if counter % args.step_size == 0 and counter != 0:
                    print('Step: ', counter)
                if line.count(',') != args.feature_size and line.count(',') != 0:
                    found_error = True
                    print("\tError in {}: Comma count: {} on line {}".format(feature_file, line.count(','), idx))
                counter += 1
        print("{}: {}".format('Invalid' if found_error else 'Valid', feature_file))

if __name__ == '__main__':
    main()
