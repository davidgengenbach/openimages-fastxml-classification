#!/usr/bin/env sh

$CAFFE_ROOT/build/tools/upgrade_net_proto_binary caffe_models/vgg_16/VGG_ILSVRC_16_layers_deploy.prototxt caffe_models/vgg_16/VGG_ILSVRC_16_layers_deploy.new.prototxt

$CAFFE_ROOT/build/tools/upgrade_net_proto_binary caffe_models/vgg_16/VGG_ILSVRC_16_layers.caffemodel caffe_models/vgg_16/VGG_ILSVRC_16_layers.new.caffemodel