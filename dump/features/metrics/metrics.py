#!/usr/bin/env python3

import tensorflow as tf
import tensorflow.contrib.losses
import helper
import sklearn.metrics
import numpy as np
import argparse

classes_1_test = './in/classes.real.test.txt'
classes_1_train = './in/classes.real.train.txt'
classes_2_test = './in/openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_test_results.txt'
classes_2_train = './in/openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_train_results.txt'

sess = None


def main():
    parser = argparse.ArgumentParser(description="Yes")
    parser.add_argument('--in1', default=classes_1_test)
    parser.add_argument('--in2', default=classes_2_test)
    parser.add_argument('--batch-size', default=10000)
    parser.add_argument('--num-labels', default=7881)
    parser.add_argument('--k', default=5)
    args = parser.parse_args()

    init_tf(args.num_labels)

    real_sp = helper.get_classes(args.in1)
    pred_sp = helper.get_classes(args.in2)

    log_losses = []
    for real, pred in helper.get_batches(real_sp, pred_sp, batch_size=args.batch_size):
        precision_at = precision_at_k(real, pred, k=args.k)
        pruned_precision_at = precision_at_k(real, pred, prune_to=0.5, k=args.k)
        log_loss = eval_tf(real, pred)
        log_losses.append(log_loss[0])
        print('LogLoss: {}\tPrecision: {}\t PrecisionPruned: {}'.format(log_loss, precision_at, pruned_precision_at))
        print()
    print('LogLossTotal: {}'.format(sum(log_losses) / len(log_losses)))


def precision_at_k(real, pred, k=5, prune_to=None):
    top_ks = []
    for idx, a in enumerate(real):
        b = pred[idx]
        real_classes = np.where(a == 1)[0]
        if prune_to:
            b[b < prune_to] = 0
        pred_classes_k = np.argsort(-b)[:k]
        similar = set(real_classes) & set(pred_classes_k)
        top_k = len(similar) / float(k)
        top_ks.append(top_k)
    return sum(top_ks) / len(top_ks)


def eval_tf(real, pred):
    return sess.run([log_loss, accuracy2], feed_dict={predictions: pred, labels: real})


def init_tf(num_labels):
    global predictions, labels, log_loss, sess, accuracy2
    predictions = tf.placeholder(tf.float32, shape=(None, num_labels))
    labels = tf.placeholder(tf.float32, shape=(None, num_labels))
    log_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(predictions, labels))

    correct_prediction = tf.equal(tf.round(tf.nn.sigmoid(predictions)), labels)
    accuracy1 = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    all_labels_true = tf.reduce_min(tf.cast(correct_prediction, tf.float32), 1)
    accuracy2 = tf.reduce_mean(all_labels_true)

    sess = tf.InteractiveSession()

if __name__ == '__main__':
    main()
