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

NUM_THREADS=$2
NUM_THREADS_TEST=$3
START_TREE=$4
NUM_TREE=$5
BIAS=$6
LOG_LOSS_COEFF=$7
MAX_LEAF=$8
LBL_PER_LEAF=$9
DATA_DIR=$10
RESULTS_DIR=$11


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
    echo "Usage: $0 NUM_THREADS NUM_THREADS_TEST START_TREE NUM_TREE BIAS LOG_LOSS_COEFF MAX_LEAF LBL_PER_LEAF DATA_DIR"
    exit
fi



EXEC_PATH="/nfs/cluster_files/dgengenbach/fast_xml/cpp-FastXML_PfastreXML/FastXML"
TRAIN_CMD="./fastXML_train"
TEST_CMD="./fastXML_test"

dataset="openimages"
#DATA_DIR="/nfs/cluster_files/dgengenbach/fast_xml"
#results_dir="$DATA_DIR/results"

train_features_file="${DATA_DIR}/cpp.fastxml.features.train.txt"
train_labels_file="${DATA_DIR}/cpp.fastxml.classes.train.txt"

test_features_file="${DATA_DIR}/cpp.fastxml.features.test.txt"
test_labels_file="${DATA_DIR}/cpp.fastxml.classes.test.txt"

SCORE_FILE_PREFIX="START_TREE__${START_TREE}__NUM_TREE__${NUM_TREE}__BIAS__${BIAS}__LOG_LOSS_COEFF__${LOG_LOSS_COEFF}__MAX_LEAF__${MAX_LEAF}__LBL_PER_LEAF__${LBL_PER_LEAF}"

score_file_test="${RESULTS_DIR}/${SCORE_FILE_PREFIX}_test_results.txt"
score_file_train="${RESULTS_DIR}/${SCORE_FILE_PREFIX}_train_results.txt"

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