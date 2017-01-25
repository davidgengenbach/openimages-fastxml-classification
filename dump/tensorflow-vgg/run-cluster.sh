IMG_PATH="/nfs/cluster_files/dgengenbach/feature_extraction/val_imgs"

ARCHIVE_PATH="/nfs/cluster_files/dgengenbach/feature_extraction"
IMG_FILE="$ARCHIVE_PATH/images.txt"
FEATURES_FILE="$ARCHIVE_PATH/features.txt"
DONE_FILE="$ARCHIVE_PATH/done.txt"
OUT="$ARCHIVE_PATH/out.log"


/nfs/cluster_files/dgengenbach/anaconda3/bin/python3 \
    test_vgg16.py \
    --images-list-file $IMG_FILE \
    --images-path $IMG_PATH \
    --done-file $DONE_FILE \
    --features-file $FEATURES_FILE
