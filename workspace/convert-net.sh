#!/usr/bin/env sh
MODEL_FOLDER="vgg16"
PROTO_TXT="$MODEL_FOLDER/VGG_ILSVRC_16_layers_deploy.new.prototxt"
CAFFEE_MODEL="$MODEL_FOLDER/VGG_ILSVRC_16_layers.new.caffemodel"
OUT_NPY="$MODEL_FOLDER/tf_net.npy"
OUT_PY="$MODEL_FOLDER/tf_net.py"

caffe-tensorflow/convert.py $PROTO_TXT --caffemodel $CAFFEE_MODEL --data-output-path=$OUT_NPY
caffe-tensorflow/convert.py $PROTO_TXT --code-output-path $OUT_PY
