import os
import pickle


def get_labels(labels, labels_npy, process = False):
    if process and os.path.exists(labels_npy):
        with open(labels_npy, 'rb') as f:
            return pickle.load(f)
    else:
        with open(labels) as f:
            images_labels = [x.strip() for x in f.read().split() if x.strip() != '']
        l = {}
        for label in images_labels:
            if label.count(',') == 2 and label.endswith(',0.0'):
                label = label.replace(',0.0', '')
            if label.count(',') != 1:
                print("Invalid line: '{}'".format(label))
                continue
            iid, label = label.split(',')
            if iid not in l:
                l[iid] = []
            l[iid].append(label)
        with open(labels_npy, 'wb') as f:
            pickle.dump(l, f)
        return l