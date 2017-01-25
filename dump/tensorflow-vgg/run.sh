IMG_PATH="../images"

IMG_FILE="$IMG_PATH/images.txt"
FEATURES_FILE="$IMG_PATH/features.txt"
DONE_FILE="$IMG_PATH/done.txt"

./test_vgg16.py \
    --images-list-file $IMG_FILE \
    --images-path $IMG_PATH \
    --done-file $DONE_FILE \
    --features-file $FEATURES_FILE
