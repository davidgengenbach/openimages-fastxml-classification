#!/usr/bin/env sh

set -x

docker run -ti --volume=$(pwd):/workspace tf-caffee:cpu bash