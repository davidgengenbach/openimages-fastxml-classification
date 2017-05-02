#!/usr/bin/env python3
'''
???
'''

PREFIX = '/nfs/cluster_files/dgengenbach/feature_extraction/val_imgs/'

def normalize(images):
    return [x.split('/')[-1].replace('.jpg', '') for x in images]

def get_img_folder_dict(images_raw):
    return {img.split('/')[-1].replace('.jpg', ''): img.split('/')[1] for img in images_raw}

def check_length(items, length):
    for item in items:
        assert(len(item) == length)

def get_as_set(file):
    with open(file) as f:
        return set([x.strip() for x in f.read().split('\n') if x.strip() != ''])

def get_image_folder(image_id, images):
    for img in set(images):
        if image_id in img:
            folder = img.split('/')[1]
            return folder
    raise Exception("No folder found for: {}".format(image_id))

features = set(normalize(get_as_set('features.ids.txt')))
images_raw = get_as_set('images.txt')
img_dict = get_img_folder_dict(images_raw)
images = set(normalize(images_raw))

check_length(features, 16)
check_length(images, 16)

diff = images - features

print('features:\t{}'.format(len(features)))
print('images:\t\t{}'.format(len(images)))
print('diff:\t\t{}'.format(len(images - features)))
print('done:\t\t{}'.format(len(images & features)))

# done.txt with prefix etc.
done = [PREFIX + img_dict[x] + '/' +  x + '.jpg' for x in images & features]
with open('done.txt', 'w') as f:
    f.write("\n".join(done))