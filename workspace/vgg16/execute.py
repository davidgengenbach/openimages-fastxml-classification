#!/usr/bin/env python

import sys
import re
import time
import numpy as np
import tensorflow as tf
from glob import glob
from scipy import misc
#sys.path.insert(0, '../caffe-tensorflow')
from tf_net import VGG_ILSVRC_16_layers

LOAD_FROM_NPY = False
LOAD_FROM_CHECKPOINT = True
SAVE_TO_CHECKPOINT = False
CHECKPOINT = "./checkpoint/tf_net.ckpt"
NPY_PATH = 'model/tf_net.npy'

t = time.time()

IMG_DIMENSIONS = (224, 224)
CHANNELS = 3
images_srcs = glob('./images/*.jpg')
images = [tf.Variable(misc.imresize(misc.imread(file), IMG_DIMENSIONS), dtype= tf.float32) for idx, file in enumerate(images_srcs)]
input_data = tf.placeholder(tf.float32, [len(images), 224, 224, CHANNELS])
net = VGG_ILSVRC_16_layers({'input': input_data})

def print_time(s, t):
    print('{}: {}ms'.format(s, int((time.time() - t) * 1000)))

with open('labels.txt', 'r') as f:
    labels = re.findall(r'.{9} (.*)', f.read())

def add_label_names(result):
    return sorted(list(zip(labels, result)), key= lambda x: x[1], reverse=True)

def get_top(result, top=5):
    return add_label_names(result)[0:top]

def get_variables_to_be_saved():
    return [var for var in tf.all_variables() if 'biases' in var.name or 'weights' in var.name]

saver = tf.train.Saver(get_variables_to_be_saved())

print_time('Init', t)

with tf.Session() as sess:
    print('Session started')
    sess.run(tf.initialize_all_variables())
    img_tf = sess.run(images)

    if LOAD_FROM_NPY:
        print("Loading from npy")
        t = time.time()
        net.load(NPY_PATH, sess)
        print_time('TimeLoadFromNpy', t)
    if LOAD_FROM_CHECKPOINT:
        print("Loading from checkpoint")
        t = time.time()
        saver.restore(sess, CHECKPOINT)
        print_time('TimeLoadFromCheckpoint', t)
    if SAVE_TO_CHECKPOINT:
        print("Saving to checkpoint")
        t = time.time()
        saver.save(sess, CHECKPOINT)
        print_time('TimeSaveCheckpoint', t)
    print('Starting prediction')

    t = time.time()
    #output = sess.run(net.get_output(), feed_dict={ input_data: img_tf })
    fc7, fc8, prob = sess.run([net.layers['fc7'], net.layers['fc8'], net.layers['prob']], feed_dict= {input_data: img_tf })
    print_time('TimePrediction', t)

    with open('probs.txt', 'w') as f:
        for idx, image in enumerate(images_srcs):
            f.write(','.join([image] + ["{:.9f}".format(x, 9) for x in prob[idx]]))

    with open('features.txt', 'w') as f:
        for idx, image in enumerate(images_srcs):
            f.write(','.join([image] + [str(x) for x in fc7[idx]] + [str(x) for x in fc8[idx]]))

    if False:
        print('\n')
        for idx, o in enumerate(output):
            print('{}'.format(images_srcs[idx]))
            for t in get_top(o, top=10):
                print('\tp={} {}'.format(round(t[1], 3), t[0]))
            print('')
