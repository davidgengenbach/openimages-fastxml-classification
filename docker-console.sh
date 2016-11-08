#!/usr/bin/env sh

set -x

docker run -ti --volume=$(pwd)/workspace:/workspace caffe-tf:cpu bash