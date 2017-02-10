#!/usr/bin/env python

# NEEDS
# - classes.sorted.txt

IN = 'out.txt'
OUT_FEATURES = 'out.features.txt'
OUT_CLASSES = 'out.classes.txt'
FEATURE_COUNT = 1000

classes_ = open('classes.sorted.txt').read().split('\n')
classes_.sort()

with open(IN) as f:
    features_and_classes = f.read().split('\n')

features_indexes = range(FEATURE_COUNT)

with open(OUT_FEATURES, 'w') as feature_file:
    feature_file.write('{} {}\n'.format(len(features_and_classes), FEATURE_COUNT))
    with open(OUT_CLASSES, 'w') as classes_file:
        classes_file.write('{} {}\n'.format(len(features_and_classes), len(classes_)))
        for line in features_and_classes:
            line = line.strip()
            if line == '':
                continue
            features, classes = line.split(' ')
            iid = features[0:16]
            features = features[17:].split(',')
            classes = classes.split(',')
            # Features
            feature_file.write(" ".join(['{}:{}'.format(idx, feature) for idx, feature in zip(features_indexes, features)]))
            feature_file.write('\n')

            # Classes

            classes_file.write(' '.join(['{}:1'.format(classes_.index(clazz)) for clazz in classes]))
            classes_file.write('\n')
