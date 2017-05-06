
# coding: utf-8

# In[64]:

import sklearn
import sklearn.metrics as metrics
from sklearn.preprocessing import MultiLabelBinarizer

import confusionmatrix as cmm
import numpy as np
from glob import glob
import sys
from time import time
import pickle
import os


# In[43]:

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


# In[6]:

def get_label_names(file = 'reference/classes.sorted.real_names.txt'):
    with open(file) as f:
        return [x.strip() for x in f.readlines() if x.strip() != '']


# In[ ]:

def get_labels_of_file(file, force_reload = False):
    pickle_name = file + '.pickle'
    if os.path.exists(pickle_name) and not force_reload:
        with open(pickle_name, 'rb') as f:
            return pickle.load(f)
    else:
        with open(file) as f:
            next(f)
            els= [[int(y.split(':')[0]) for y in x.split(' ')] for x in f.read().split('\n') if x.strip() != '']
            
            with open(pickle_name, 'wb') as f:
                pickle.dump(els, f)
            return els


# In[68]:

def get_scores(y_true, y_pred_filename, labels):
    y_pred = get_labels_of_file(y_pred_filename, force_reload = False)
    assert(len(y_pred) == len(y_true)) #, 'Length of y_pred and y_true must be same! train/test wrong?')
    mlb = MultiLabelBinarizer().fit([range(len(labels))])
    y_pred_t = mlb.transform(y_true)
    y_true_t = mlb.transform(y_pred)
    return (
            metrics.classification_report(y_true_t, y_pred_t),
            metrics.f1_score(y_true_t, y_pred_t, average = 'macro'),
            metrics.coverage_error(y_true_t, y_pred_t)
    )


# In[21]:

labels = get_label_names()
y_true_train = get_labels_of_file('reference/classes.real.train.txt', False)
y_true_test = get_labels_of_file('reference/classes.real.test.txt', False)


# In[70]:

for file in glob('results/*_results.txt'):
    y_true_used = y_true_test if file.count('test_results') == 1 else y_true_train
    file_size = os.path.getsize(file)
    print("# {} ({})".format(file, sizeof_fmt(file_size)))
    sys.stdout.flush()
    scores = get_scores(y_true_used, file, labels = labels)

    print(scores)
    sys.stdout.flush()

