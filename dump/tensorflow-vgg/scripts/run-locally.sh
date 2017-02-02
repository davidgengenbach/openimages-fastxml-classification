IMG_PATH="../data/images"

IMG_FILE="$IMG_PATH/images.txt"
FEATURES_FILE="$IMG_PATH/features.txt"
DONE_FILE="$IMG_PATH/done.txt"

BATCH_SIZE=2

./test_vgg16.py \
    --images-list-file $IMG_FILE \
    --images-path $IMG_PATH \
    --done-file $DONE_FILE \
    --batch-size $BATCH_SIZE \
    --features-file $FEATURES_FILE
