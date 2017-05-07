#!/usr/bin/env python3
'''
???
'''
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Create done.txt with all the finished images')
    parser.add_argument('--images-list', type=str, help="The raw image list", default='images.txt')
    parser.add_argument('--feature-ids-list', type=str,
                        help="A text file with only the image ids in it", default='features.ids.txt')
    parser.add_argument('--done-file', type=str,
                        help="A text file with only the image ids in it that are also done", default='done')
    parser.add_argument('--image-prefix', type=str, help="A text file with only the image ids in it that are also done",
                        default='/nfs/cluster_files/dgengenbach/ml-praktikum/data/val_imgs/')
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    features = set(normalize(get_as_set(args.feature_ids_list)))
    images_raw = get_as_set(args.images_list)
    img_dict = get_img_folder_dict(images_raw)
    images = set(normalize(images_raw))

    check_length(features, 16)
    check_length(images, 16)

    diff = images - features

    print('features:\t{}'.format(len(features)))
    print('images:\t\t{}'.format(len(images)))
    print('diff:\t\t{}'.format(len(images - features)))
    print('done:\t\t{}'.format(len(images & features)))

    # done.txt with prefix etc.
    done = [args.image_prefix + img_dict[x] + '/' + x + '.jpg' for x in images & features]
    with open(args.done_file, 'w') as f:
        f.write("\n".join(done))


def check_length(items, length):
    for item in items:
        assert(len(item) == length)


def get_as_set(file):
    with open(file) as f:
        return set([x.strip() for x in f.read().split('\n') if x.strip() != ''])


def get_image_folder(image_id, images):
    for img in set(images):
        if image_id in img:
            folder = img.split('/')[1]
            return folder
    raise Exception("No folder found for: {}".format(image_id))


def normalize(images):
    return [x.split('/')[-1].replace('.jpg', '') for x in images]


def get_img_folder_dict(images_raw):
    return {img.split('/')[-1].replace('.jpg', ''): img.split('/')[1] for img in images_raw}


if __name__ == '__main__':
    main()
