#!/usr/bin/env python3

import numpy as np

k = 5


real = np.array([[0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]])
pred = np.array([[0.5, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]])

pred[pred < 0.5] = 0
print(pred)
exit

for idx, a in enumerate(real):
    b = pred[idx]
    real_classes = np.where(a == 1)[0]
    pred_classes_k = np.argsort(-b)[:k]
    similar = set(real_classes) & set(pred_classes_k)
    print(len(similar) / float(k))
