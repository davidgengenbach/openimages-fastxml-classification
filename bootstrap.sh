#!/usr/bin/env bash

HERE=$(pwd -P)

INIT_GITSUBMODULES=0
DOWNLOAD_ANNOTATIONS=0
# Does not work anymore, the download was disabled!
DOWNLOAD_IMAGES=0
DOWNLOAD_VGG_MODELS=1

back () {
    cd "$HERE"
}

if [ "$INIT_GITSUBMODULES" -eq 1 ]; then
    git submodule update --init --recursive
fi

if [ "$DOWNLOAD_ANNOTATIONS" -eq 1 ]; then
    cd dataset
    ../tmp/bootstrap/download-dataset.sh
    back
fi

if [ "$DOWNLOAD_IMAGES" -eq 1 ]; then
    ./tmp/bootstrap/download-openimages.sh
    back
fi

if [ "$DOWNLOAD_VGG_MODELS" -eq 1 ]; then
    # URLs for vgg models
    VGG16_NPY="https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM"
    VGG19_NPY="https://mega.nz/#!xZ8glS6J!MAnE91ND_WyfZ_8mvkuSa2YcA7q-1ehfSm-Q1fxOvvs"
    ./tmp/bootstrap/download-model.sh $VGG16_NPY vgg/tensorflow-vgg/vgg16.npy
    ./tmp/bootstrap/download-model.sh $VGG19_NPY vgg/tensorflow-vgg/vgg19.npy
fi

