# Dataset
[OpenImages Dataset](https://github.com/openimages/dataset)

## images
- CSV Headers
    - 1  ImageID
    - 2  Subset
    - 3  OriginalURL
    - 4  OriginalLandingURL
    - 5  License
    - 6  AuthorProfileURL
    - 7  Author
    - 8  Title
    - 9  OriginalSize
    - 10 OriginalMD5
    - 11 Thumbnail300KURL
- train
    - Total:      9.011.220
    - Size:       18.3 TB
- validation
    - Total:      167.057
    - Size:       309.9 GB

## annotations
- CSV Headers
    - 1 ImageID
    - 2 Source
    - 3 LabelName
    - 4 Confidence
- MISPREDICTED
    - Ratio:  31% (false positives)
    - Most:   "produce, flower, plant, food, sports, shrub, human body"
- human
    - validation
        - Total:      1.741.385
        - Confidences:
            - 0.0     31.5%
            - 1.0     68.5%
        - Images that have no positive label: ca. 2000

- machine
    - validation
        - Total:      2.060.221
        - Confidences:
            - 0.5     14.5%
            - 0.6     22.2%
            - 0.7     20.5%
            - 0.8     17.4%
            - 0.9     18.4%
            - 1.0      7.0%
    - train
        - Total:      79.196.416
        - Confidences:
            - 0.5     12.3%
            - 0.6     22.0%
            - 0.7     21.3%
            - 0.8     20.5%
            - 0.9     19.8%
            - 1.0      4.0%

## Useful commands

**Headers**

head -n 1 $FILE

**Linecount**

wc -l $FILE

**Extract 4th column**

cat $FILE | cut -d , -f 4 > $NEW_FILE

**http://bconnelly.net/working-with-csvs-on-the-command-line/**

[working-with-data-on-the-command-line](http://www.datamazing.co.uk/2014/01/25/working-with-data-on-the-command-line)

cat file.csv | sed -e 's/,,/, ,/g' | column -s, -t

**Top10 mispredicted**

head -n 10 download/human_ann_2016_08/validation/labels_mispredicted_wc.csv | cut -d , -f 1 | ./labelnames.sh

cat labels.csv | grep -E '/m/036qh8.*,0.0' > labels_mispredicted_wc2.csv