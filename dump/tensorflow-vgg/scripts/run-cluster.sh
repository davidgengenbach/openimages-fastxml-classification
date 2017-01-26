cd ..

IMG_PATH="/nfs/cluster_files/dgengenbach/feature_extraction/val_imgs"

WORK_DIR="/nfs/cluster_files/dgengenbach/feature_extraction"
IMG_FILE="$WORK_DIR/images.txt"
FEATURES_FILE="$WORK_DIR/features.txt"
DONE_FILE="$WORK_DIR/done.txt"


/nfs/cluster_files/dgengenbach/anaconda3/bin/python3 \
    test_vgg16.py \
    --images-list-file $IMG_FILE \
    --images-path $IMG_PATH \
    --done-file $DONE_FILE \
    --features-file $FEATURES_FILE
