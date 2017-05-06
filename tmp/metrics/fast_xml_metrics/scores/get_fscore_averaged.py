
# coding: utf-8

# In[1]:

#!jupyter nbconvert --to script get_fscore_averaged.ipynb


# In[8]:

import confusionmatrix as cmm
import numpy as np
from glob import glob
import sys
from time import time
import pickle
import os


# In[ ]:

#if len(sys.argv) < 2:
#    sys.exit(1)
    
#FILE = sys.argv[1]


# In[3]:

def print_time(start_time, msg = ''):
    print('Time: {:.4f} {}'.format(time() - start_time, msg))


# In[33]:

def get_classes(file, num_elements = 1000, force_reload = False):
    pickle_name = file + '.pickle'
    if os.path.exists(pickle_name) and not force_reload:
        with open(pickle_name, 'rb') as f:
            return pickle.load(f)
    else:
        with open(file) as f:
            next(f)
            els= [[(int(y.split(':')[0]), float(y.split(':')[1])) for y in x.split(' ')] for x in f.read().split('\n') if x.strip() != '']
            return els if num_elements == None else els[0:num_elements]


# In[36]:

def get_real_pred(filename, is_test):
    test_str = 'test' if is_test else 'train'
    PRED = filename.format(test_str)

    NUM_ELEMENTS = None
    pred_ = get_classes(PRED, NUM_ELEMENTS)
    if isinstance(pred_, tuple):
        return pred_
    
    for idx,pred in enumerate(pred_):
        pred_[idx] = [x for x in pred]

    real_ = get_classes('reference/classes.real.{}.txt'.format(test_str), NUM_ELEMENTS)
    assert(len(real_) == len(pred_))

    def get_classes_only(x):
        return [[p[0] for p in y] for y in x]
    vals = get_classes_only(pred_), get_classes_only(real_)
    with open(PRED + '.pickle', 'wb') as f:
        pickle.dump(vals, f)
    return vals


# In[6]:

def get_average(real_, pred_):
    cm = cmm.ConfusionMatrix() 
    for gold, pred in list(zip(real_, pred_)):
        cm.add(gold, pred)
    return cm.averaged(level = cmm.MICRO, score=cmm.FSCORE)


# In[1]:

all_files = set(glob('../results/*_results.txt'))

DONE = False
for filename in all_files:
    if DONE:
        continue
    with open('../metrics.txt') as f:
        if filename.split('/')[-1] in f.read():
            continue
    IS_TEST = filename.count('test_results') == 1
    value = get_real_pred(filename, is_test = IS_TEST)
    print('{} {}'.format(filename, get_average(*value)))
    sys.stdout.flush()
    os.rename(filename, filename.replace('results/', 'results/done/'))
    DONE = True


# In[ ]:



