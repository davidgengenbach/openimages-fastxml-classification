#!/usr/bin/env python3

import numpy as np
import tensorflow as tf

import helper
import time
import vgg19
import utils

args = helper.get_args(description='Extract VGG19 features')
helper.setup(args)

batch_size = args.batch_size

with tf.Session() as sess:
    vgg = vgg19.Vgg19()
    images = tf.placeholder("float", [None, 224, 224, 3])
    vgg.build(images)
    for img_paths, imgs in helper.next_img_batch(
            count=batch_size,
            done_file=args.done_file,
            images_file=args.images_list_file,
            prepend_image_path=args.images_path
        ):
        t = time.time()

        fc7_output, fc8_output = sess.run([vgg.fc7, vgg.fc8], feed_dict={images: imgs})

        helper.save_features(img_paths, [fc7_output, fc8_output], features_file=args.features_file)
        print('{:.3f} seconds/image'.format((time.time() - t) / batch_size))
        sys.stdout.flush()
