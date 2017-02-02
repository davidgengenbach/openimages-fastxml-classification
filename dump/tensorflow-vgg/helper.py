import numpy as np
import os
import scipy
import scipy.misc
import sys
import time
import pickle
import argparse
from glob import glob
import datetime
import skimage
import skimage.io
import skimage.color


def get_args(description="Generic description"):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--images-list-file', default='images/files.txt')
    parser.add_argument('--images-path', default='')
    parser.add_argument('--done-file', default='images/done.txt')
    parser.add_argument('--features-file', default='images/features.txt')
    parser.add_argument('--batch-size', default=16, type=int)
    args = parser.parse_args()
    args.features_file = get_features_file_stamped_filename(args.features_file)
    return args


def setup(args):
    if not os.path.exists(args.images_list_file):
        print('Image file not existent: {}'.format(args.images_list_file))
        sys.exit(1)

    if not os.path.exists(args.done_file):
        open(args.done_file, 'a').close()

    if not os.path.exists(args.features_file):
        open(args.features_file, 'a').close()


def next_img_batch(count=10, done_file='images/done.txt', images_file='images/files.txt', prepend_image_path=''):
    if prepend_image_path != '' and prepend_image_path[-1] != '/':
        prepend_image_path = prepend_image_path + '/'
    files = [prepend_image_path + x.replace('./', '') for x in get_filecontent_as_set(images_file) if x.strip() != '']
    for imgs in get_next_batch(files, done_file, count=count):
        add_set_to_file(done_file, imgs)
        yield transform_images(imgs)

def get_filecontent_as_set(file):
    with open(file) as f:
        return set(f.read().split('\n'))


def add_set_to_file(file, data):
    with open(file, 'a') as f:
        f.write('\n' + "\n".join(data))


def get_next_batch(files, done_file, count=100):
    done = get_filecontent_as_set(file=done_file)
    items = []
    for item in files:
        if item not in done and item.strip() != '':
            items.append(item)
            if len(items) == count:
                yield items
                done = get_filecontent_as_set(file=done_file)
                items = []


def save_features(filenames, features, features_file):
    save_features_normal(filenames, features, features_file)


def save_features_normal(filenames, features, features_file):
    lock_file = features_file + '.lock'
    while os.path.exists(lock_file):
        time.sleep(0.1)

    with open(lock_file, 'w') as f:
        pass

    with open(features_file, 'a') as f:
        f.write('\n')

        for idx, filename in enumerate(filenames):
            features_ = np.append(features[0][idx], features[1][idx])
            f.write(','.join([filename.split('/')[-1].replace('.jpg', '')] + [str(x) for x in features_]))
            f.write('\n')

    os.remove(lock_file)


def transform_images(img_paths):
    imgs_transformed = []
    img_paths_ = []
    for img in img_paths:
        if img.strip() == '':
            continue
        try:
            imgs_transformed.append(transform_image(img).reshape((1, 224, 224, 3)))
            img_paths_.append(img)
        except Exception as e:
            print(e)
    return (img_paths_, np.concatenate(imgs_transformed, 0))


def transform_image(img, over_sample=False, mean_pix=[103.939, 116.779, 123.68], image_dim=256, crop_dim=224, subtract_mean=False, divide_by_255=True):

    img_filename = img
    img = np.array(skimage.io.imread(img))

    if len(img.shape) == 2:
        img = skimage.color.gray2rgb(img)

    #assert((0 <= img).all() and (img <= 1.0).all())
    #img = np.roll(img, 1, axis=-1)
    # resize image, the shorter side is set to image_dim
    if img.shape[0] < img.shape[1]:
        dsize = (int(np.floor(float(image_dim)*img.shape[1]/img.shape[0])), image_dim)
    else:
        dsize = (image_dim, int(np.floor(float(image_dim)*img.shape[0]/img.shape[1])))

    dsize = (dsize[1], dsize[0])

    # @see https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imresize.html
    img = scipy.misc.imresize(img, dsize)  # , interp='bicubic')

    # convert to float32
    img = img.astype(np.float32, copy=False)

    # crop
    indices_y = [0, img.shape[0]-crop_dim]
    indices_x = [0, img.shape[1]-crop_dim]
    center_y = int(np.floor(indices_y[1]/2))
    center_x = int(np.floor(indices_x[1]/2))
    try:
        img = img[center_y:center_y + crop_dim, center_x:center_x+crop_dim, :]
        if subtract_mean:
            for i in range(3):
                img[:, :, i] -= mean_pix[i]
        if divide_by_255:
            img /= 255
    except Exception as e:
        raise Exception("Error Processing image: {}\nException: {}".format(img_filename, e))
    return img


def get_features_file_stamped_filename(features_filename):
    parts = features_filename.split('.')
    if 'SLURM_JOB_ID' in os.environ:
        stamp = os.environ['SLURM_JOB_ID']
    else:
        stamp = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
    parts.insert(-1, stamp)
    return ".".join(parts)


def save_features_pickle(filenames, features, features_file):
    with open(features_file, 'ab') as f:
        for idx, filename in enumerate(filenames):
            features_ = np.append(features[0][idx], features[1][idx])
            pickle.dump(','.join([filename.split('/')[-1].replace('.jpg', '')] + [str(x) for x in features_]), f)
