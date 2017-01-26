#!/usr/bin/env python3

import tensorflow as tf
import numpy as np
import time
import sys
import helper
import argparse
import os
import datetime

import vgg16
import utils

parser = argparse.ArgumentParser(description='Extract VGG16 features')
parser.add_argument('--images-list-file', default='images/files.txt')
parser.add_argument('--images-path', default='')
parser.add_argument('--done-file', default='images/done.txt')
parser.add_argument('--features-file', default='images/features.txt')
args = parser.parse_args()

def get_features_file_stamped(features_file):
    parts = features_file.split('.')
    if 'SLURM_JOB_ID' in os.environ:
        stamp = os.environ['SLURM_JOB_ID']
    else:
        stamp = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
    parts.insert(-1, stamp)
    return ".".join(parts)

args.features_file = get_features_file_stamped(args.features_file)


if not os.path.exists(args.images_list_file):
    print('Image file not existent: {}'.format(args.images_list_file))
    sys.exit(1)

if not os.path.exists(args.done_file):
    open(args.done_file, 'a').close()

if not os.path.exists(args.features_file):
    open(args.features_file, 'a').close()

print_probs = False

batch_size = 16

with tf.Session() as sess:
    vgg = vgg16.Vgg16()
    images = tf.placeholder("float", [batch_size, 224, 224, 3])
    vgg.build(images)
    for batch_imgs in helper.next_img_batch(count=batch_size, done_file=args.done_file, images_file=args.images_list_file, prepend_image_path=args.images_path):
        if len(batch_imgs) < batch_size:
            break
        t = time.time()
        imgs_transformed = [helper.transform_image(x).reshape((1, 224, 224, 3)) for x in batch_imgs if x.strip() != '']
        batch = np.concatenate(imgs_transformed, 0)
        feed_dict = {images: batch}
        fc7_output, fc8_output = sess.run([vgg.fc7, vgg.fc8], feed_dict=feed_dict)

        helper.save_features(batch_imgs, [fc7_output, fc8_output], features_file=args.features_file)
        print('{:5f} seconds per image'.format((time.time() - t) / batch_size))
        sys.stdout.flush()
