
# coding: utf-8

# In[1]:

import numpy as np


# In[13]:

def get_lines_of_file(file, remove_empty = True):
    with open(file) as f:
        return [x.strip() for x in f.readlines() if remove_empty and x.strip() != '']

def get_label_map(file = 'reference/dict.csv'):
    return {x.split('","')[0].replace('"', '').strip(): x.split('","')[1].replace('"', '').strip()  for x in get_lines_of_file(file)}


# In[17]:

labels = get_lines_of_file('reference/classes.sorted.txt')
label_map = get_label_map()
label_names = []
for label in labels:
    if label not in label_map:
        print('Label not found: {}'.format(label))
    label_names.append(label_map[label])

with open('reference/classes.sorted.real_names.txt', 'w') as f:
    f.write("\n".join(label_names))

