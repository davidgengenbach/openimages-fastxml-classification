#!/usr/bin/env sh

FOLDER='vgg16'

upgrade_net_proto_binary $FOLDER/VGG_ILSVRC_16_layers.caffemodel $FOLDER/VGG_ILSVRC_16_layers.new.caffemodel
upgrade_net_proto_text $FOLDER/VGG_ILSVRC_16_layers_deploy.prototxt $FOLDER/VGG_ILSVRC_16_layers_deploy.new.prototxt