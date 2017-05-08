
# coding: utf-8

# In[3]:

import numpy as np


# In[10]:

NUM_ELEMENTS = 40000
MIN_LABELS = 1
MAX_LABELS = 10

FROM_LABEL = 1
TO_LABEL = 500


# In[8]:

out = []
for i in range(NUM_ELEMENTS):
    outt = []
    NUM_LABELS = np.random.randint(MIN_LABELS, MAX_LABELS + 1)
    for ii in range(NUM_LABELS):
        outt.append('{}:1'.format(np.random.randint(FROM_LABEL, TO_LABEL + 1)))
    out.append(" ".join(outt))
np.random.shuffle(out)
with open('cpp.fastxml.small.classes.txt', 'w') as f:
    f.write("\n".join(out))

