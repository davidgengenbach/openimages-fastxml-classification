#!/usr/bin/env python3

FEATURE_FILE = 'features.ids.txt'
IMAGES_FILE = 'images.txt'

IMAGE_PREFIX = '/nfs/cluster_files/dgengenbach/feature_extraction/val_imgs/'

def get_file_splitted(file):
	return [x for x in open(file, 'r').read().split('\n') if x.strip() != '']

features = get_file_splitted(FEATURE_FILE)

images = {x.split('/')[-1].replace('.jpg', ''): x.replace('./', '').split('/')[1] for x in get_file_splitted(IMAGES_FILE)}
diff  = list(set(images.keys()).intersection(set(features)))

with open('done.new.txt', 'w') as f:
	f.write("\n".join([IMAGE_PREFIX + x + '.jpg' for x in diff]))
#print(len(diff), len(images))
#print(features[0:10], images[0:10])
#diff = list(set(images).intersection(set(features)))

#with open('done.txt', 'w') as f:
#	f.write("\n".join(features))
