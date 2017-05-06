#!/usr/bin/env bash

set -e

cd ..

# Extract features
./test_vgg16.py --images-list-file test/images.txt --done-file test/done.txt --features-file test/features.txt

HERE=$(pwd -P)

# Convert to FastXML
FEATURES_FILE="$(pwd)/$(ls test/features* | sort -r | head -n 1 | awk '{$1=$1};1')"
./test/add_bogus_label.py
# ...
echo >> $FEATURES_FILE

cd /Users/davidgengenbach/Documents/Projekte/ml-praktikum/dump/data
#./add_classes_to_features.py --features-file $FEATURES_FILE
./cpp_fastxml_format.py --features-labels-file $FEATURES_FILE
scp out/cpp.fastxml.features.txt ke:./cluster_files/fast_xml
cd "$HERE"

# On server
ssh ke 

if [ 0 -eq 1 ]; then
    ssh kenode52
    cd /nfs/cluster_files/dgengenbach/fast_xml/cpp-FastXML_PfastreXML/FastXML && ./fastXML_test /nfs/cluster_files/dgengenbach/fast_xml/cpp.fastxml.features.txt /nfs/cluster_files/dgengenbach/fast_xml/RESULTS.txt /nfs/cluster_files/dgengenbach/fast_xml/cpp-FastXML_PfastreXML/FastXML/../Sandbox/Results/openimages/model -T 4
fi

# Copy down
cd $HERE
cat test/images.txt
cd /Users/davidgengenbach/Documents/Projekte/ml-praktikum/dump/features/metrics/
scp ke:/nfs/cluster_files/dgengenbach/fast_xml/RESULTS.txt in/
./get_label_of_result.py --results-file in/RESULTS.txt