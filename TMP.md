```bash
./tmp/feature_extraction/extract_feature_ids.sh data/features.fc7.ids.txt data/features.fc7.2017*.txt;
echo "Done"
./tmp/feature_extraction/check_feature_ids.py --images-list data/images.txt --feature-ids-list data/features.fc7.ids.txt --done-file data/done.fc7.txt --image-prefix $(pwd)/data/val_imgs/
```