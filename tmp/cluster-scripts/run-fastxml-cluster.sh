#!/bin/bash

DEBUG=1
MODE=$1

if [ "$DEBUG" == 1 ]; then
    set -x
fi

if [ -z "$MODE" ]; then
    MODE="train"
fi

echo "Mode: $MODE"

DATA_DIR=$2
RESULTS_DIR="$DATA_DIR/results"

NUM_THREADS=$3
NUM_THREADS_TEST=$4
START_TREE=$5
NUM_TREE=$6
BIAS=$7
LOG_LOSS_COEFF=$8
MAX_LEAF=$9
LBL_PER_LEAF=$10


if [ -z "$NUM_THREADS"] ||
[ -z "$NUM_THREADS_TEST"] ||
[ -z "$START_TREE"] ||
[ -z "$NUM_TREE"] ||
[ -z "$BIAS"] ||
[ -z "$LOG_LOSS_COEFF"] ||
[ -z "$MAX_LEAF"] ||
[ -z "$LBL_PER_LEAF"] ||
[ -z "$DATA_DIR"] ||
[ -z "$RESULTS_DIR"]; then
    echo "Usage: $0 data_dir num_threads num_threads_test start_tree num_tree bias log_loss_coeff max_leaf lbl_per_leaf"
    exit
fi


EXEC_PATH="/nfs/cluster_files/dgengenbach/ml-praktikum/fastxml/cpp-FastXML_PfastreXML/FastXML"
TRAIN_CMD="./fastXML_train"
TEST_CMD="./fastXML_test"

train_features_file="${DATA_DIR}/cpp.fastxml.features.train.txt"
train_labels_file="${DATA_DIR}/cpp.fastxml.classes.train.txt"

test_features_file="${DATA_DIR}/cpp.fastxml.features.test.txt"
test_labels_file="${DATA_DIR}/cpp.fastxml.classes.test.txt"

SCORE_FILE_PREFIX="start_tree__${START_TREE}__num_tree__${NUM_TREE}__bias__${BIAS}__log_loss_coeff__${LOG_LOSS_COEFF}__max_leaf__${MAX_LEAF}__lbl_per_leaf__${LBL_PER_LEAF}"

score_file_test="${RESULTS_DIR}/${SCORE_FILE_PREFIX}-results.test.txt"
score_file_train="${RESULTS_DIR}/${SCORE_FILE_PREFIX}-results.train.txt"

model_dir="$RESULTS_DIR/model/$SCORE_FILE_PREFIX"
mkdir "$model_dir"

cd $EXEC_PATH

# training
if [ "$MODE" == "train" ]; then
    $TRAIN_CMD \
        $train_features_file \
        $train_labels_file \
        $model_dir \
        -T $NUM_THREADS \
        -s $START_TREE \
        -t $NUM_TREE \
        -b $BIAS \
        -c $LOG_LOSS_COEFF \
        -m $MAX_LEAF \
        -l $LBL_PER_LEAF
fi
# testing
if [ "$MODE" == "test" ]; then
    $TEST_CMD \
        $test_features_file \
        $score_file_test \
        $model_dir \
        -T $NUM_THREADS_TEST

    $TEST_CMD \
        $train_features_file \
        $score_file_train \
        $model_dir \
        -T $NUM_THREADS_TEST
fi


# -T
#       num_thread
#       Number of threads to use
#       (default=1)
# -s
#       start_tree
#       Starting tree index
#       (default=0)
# -t
#       num_tree
#       Number of trees to be grown
#       (default=50)
# -b
#       bias
#       Feature bias value, extre feature value to be appended
#       (default=1.0)
# -c
#       log_loss_coeff
#       SVM weight co-efficient
#       (default=1.0)
# -l
#       lbl_per_leaf
#       Number of label-probability pairs to retain in a leaf
#       (default=100)
# -m
#       max_leaf
#       Maximum allowed instances in a leaf node.
#       Larger nodes are attempted to be split,
#       and on failure converted to leaves
#       (default=10)