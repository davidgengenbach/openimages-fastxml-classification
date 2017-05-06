#!/usr/bin/env python3

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='desc')
    parser.add_argument('--features-file', type=str, help="features.ids.txt")
    parser.add_argument('--images-file', type=str, help="images.txt")
    parser.add_argument('--images-prefix', type=str, help="/nfs/cluster_files/dgengenbach/ml-praktikum/data/val_imgs/")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    features = get_file_splitted(args.features_file)

    images = {x.split('/')[-1].replace('.jpg', ''): x.replace('./', '').split('/')[1]
              for x in get_file_splitted(args.images_file)}
    diff = list(set(images.keys()).intersection(set(features)))

    with open('done.new.txt', 'w') as f:
        f.write("\n".join([args.images_prefix + x + '.jpg' for x in diff]))


def get_file_splitted(file):
    return [x for x in open(file, 'r').read().split('\n') if x.strip() != '']

if __name__ == '__main__':
    main()
