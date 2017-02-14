#!/bin/bash

dataset="openimages"
data_dir="/root/data/out"
results_dir="../Sandbox/Results/$dataset"
model_dir="../Sandbox/Results/$dataset/model"

trn_ft_file="${data_dir}/cpp.fastxml.features.txt"
trn_lbl_file="${data_dir}/cpp.fastxml.classes.txt"
#tst_ft_file="${data_dir}/tst_X_Xf.txt"
#tst_lbl_file="${data_dir}/tst_X_Y.txt"
score_file="${results_dir}/score_mat.txt"

# training
# Reads training features (in $trn_ft_file), training labels (in $trn_lbl_file), and writes FastXML model to $model_dir
./fastXML_train $trn_ft_file $trn_lbl_file $model_dir -T 4 -s 0 -t 50 -b 1.0 -c 1.0 -m 10 -l 10

# -T    num_thread      (default=1)
#        Number of threads to use
# -s    start_tree      (default=0)
#        Starting tree index
# -t    num_tree        (default=50)
#        Number of trees to be grown
# -b    bias        (default=1.0)
#        Feature bias value, extre feature value to be appended
# -c    log_loss_coeff      (default=1.0)
#        SVM weight co-efficient
# -l    lbl_per_leaf        (default=100)
#        Number of label-probability pairs to retain in a leaf
# -m    max_leaf        (default=10)
#        Maximum allowed instances in a leaf node. Larger nodes are attempted to be split, and on failure converted to leaves

# testing
# Reads test features (in $tst_ft_file), FastXML model (in $model_dir), and writes test label scores to $score_file
./fastXML_test $trn_ft_file $score_file $model_dir
#./fastXML_test $tst_ft_file $score_file $model_dir

# performance evaluation
#matlab -nodesktop -nodisplay -r "cd('$PWD'); addpath(genpath('../Tools')); trn_X_Y = read_text_mat('$trn_lbl_file'); tst_X_Y = read_text_mat('$tst_lbl_file'); wts = inv_propensity(trn_X_Y,0.55,1.5); score_mat = read_text_mat('$score_file'); get_all_metrics(score_mat, tst_X_Y, wts); exit;"

