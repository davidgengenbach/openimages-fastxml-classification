#!/usr/bin/env python3
'''
Calculates metrics on a given FastXML result file.
'''


import helper
import sklearn.metrics
import numpy as np
import argparse
from time import time
from glob import glob

classes_1_test = './in/classes.real.test.txt'
classes_1_train = './in/classes.real.train.txt'
classes_2_test = './in/openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_test_results.txt'
classes_2_train = './in/openimages__NUM_THREADS__1__START_TREE__0__NUM_TREE__50__BIAS__1.0__LOG_LOSS_COEFF__1.0__MAX_LEAF__50__LBL_PER_LEAF__10_train_results.txt'

sess = None


def get_args():
    parser = argparse.ArgumentParser(description="Calculates metrics on sparse matrix results from FastXML")
    parser.add_argument('--in1', default=classes_1_train)
    parser.add_argument('--in2', default=classes_2_train)
    parser.add_argument('--batch-size', default=10000)
    parser.add_argument('--num-labels', default=7881)
    parser.add_argument('--k', default=5)
    parser.add_argument('--prune-to', default=0.1, type=float)
    parser.add_argument('--eval-tf', default=False, type=bool)
    parser.add_argument('--use-pickle', default=False, type=bool)
    return parser.parse_args()


def main():
    args = get_args()

    if args.eval_tf:
        init_tf(args.num_labels)

    real_sp = helper.get_classes(args.in1, re_read = not args.use_pickle)
    results = []
    for file in glob(args.in2):
        print('# {}'.format(file))
        pred_sp = helper.get_classes(file, re_read = not args.use_pickle)
        assert(real_sp.shape == pred_sp.shape)

        results = []
        for real, pred in helper.get_batches(real_sp, pred_sp, batch_size=args.batch_size):

            # Precision at k
            precision_at = precision_at_k(real, pred, k=args.k)
            #pruned_precision_at = precision_at_k(real, pred, prune_to=args.prune_to, k=args.k)
            #print('Precision: {:.4f}\nPrecisionPruned: {:.4f}'.format(precision_at, pruned_precision_at))
            #results.append((precision_at, pruned_precision_at))
            results.append(precision_at)
            # Logloss
            if args.eval_tf:
                log_loss = eval_tf(real, pred)
                log_losses.append(log_loss[0])
                print('LogLoss: {:<4}'.format(", ".join([str(x)[0:4] for x in log_loss])))

        def get_total_precision(results, column):
            #precisions = np.array(results)[:, column]
            precisions = results
            return sum(precisions) / len(precisions)

        print('Total Precision@{}: {}'.format(
            args.k,
            get_total_precision(results, 0)
        ))
        #print('LogLossTotal: {}'.format(sum(log_losses) / len(log_losses)))


def precision_at_k(real, pred, k=5, prune_to=None):
    top_ks = []
    for idx, a in enumerate(real):
        b = pred[idx]
        real_classes = np.where(a == 1)[0]
        # if prune_to:
        #    b[b < prune_to] = 0
        #pred_classes_k_old = np.argsort(-b)[:k]
        pred_classes_k = np.argpartition(b, -k)[-k:]
        assert(len(pred_classes_k) == k)
        if prune_to:
            pred_classes_k = [x for x in pred_classes_k if b[x] > prune_to]
        # if prune_to:
        #    b[b < prune_to] = 0
        similar = set(real_classes) & set(pred_classes_k)
        top_k = len(similar) / min(float(k), len(real_classes))
        top_ks.append(top_k)
    return sum(top_ks) / len(top_ks)


def eval_tf(real, pred):
    metrics = [log_loss, accuracy1, accuracy2, accuracy3, update_op1]
    metrics = [log_loss]
    return sess.run(metrics, feed_dict={predictions: pred, labels: real})


def init_tf(num_labels):
    import tensorflow as tf
    import tensorflow.contrib.losses
    global predictions, labels, log_loss, sess, accuracy1, update_op1, accuracy2, accuracy3
    predictions = tf.placeholder(tf.float32, shape=(None, num_labels))
    labels = tf.placeholder(tf.float32, shape=(None, num_labels))
    #log_loss = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    #log_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=predictions, labels=labels))

    log_loss = tf.losses.log_loss(labels=labels, predictions=predictions)

    correct_prediction = tf.equal(tf.round(tf.nn.sigmoid(predictions)), labels)
    accuracy1, update_op1 = tf.metrics.accuracy(labels=labels, predictions=predictions)
    #accuracy1 = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    all_labels_true = tf.reduce_min(tf.cast(correct_prediction, tf.float32), 1)
    accuracy2 = tf.reduce_mean(all_labels_true)
    accuracy3 = tf.reduce_mean(tf.cast(tf.round(predictions) == labels, tf.float32))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())

if __name__ == '__main__':
    main()

#pred = 1 / (1 + np.exp(-pred))
