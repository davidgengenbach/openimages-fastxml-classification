import scipy
import scipy.sparse
import numpy as np
import math
import sklearn.metrics
import os
import pickle
from scipy import sparse, io


def get_classes(file, verbose=False, eps=1e-10, test=False, re_read=False):
    file_parts = file.split('/')
    file_parts.append(file_parts[-1] + '.pickle')
    file_parts[-2] = 'pickle'
    pickle_file = "/".join(file_parts)
    #pickle_file = file + '.pickle'

    if not re_read and os.path.exists(pickle_file):
        mat = pickle.load(open(pickle_file, 'rb'))
    else:
        elements = []
        with open(file) as f:
            num_elements, num_classes = f.readline().split(' ')
            elements = f.read().strip().split('\n')
            #elements = elements[0:10000]
            num_elements = len(elements)
            num_classes = int(num_classes)
        classes = []
        data = []
        indices = []
        indptr = []
        for idx, element in enumerate(elements):
            if verbose and (idx % STEP == 0 or idx == num_elements - 1):
                print("\tElement: {:>14}/{}".format(idx, num_elements))

            if test and element.strip() == '':
                print("Empty element? {}".format(idx))

            clazzes = []
            for clazz in element.split(' '):
                clazz_idx, val = clazz.split(':')
                clazz_idx = int(clazz_idx)
                val = float(val)

                data.append(val)
                if test and not val >= 0 or not val <= 1:
                    print("Invalid val: {}".format(val))
                indptr.append(idx)
                indices.append(clazz_idx)

        mat = scipy.sparse.csc_matrix((data, (indptr, indices)), shape=(num_elements, num_classes), dtype=np.float32)
        pickle.dump(mat, open(pickle_file, 'wb'), pickle.HIGHEST_PROTOCOL)
    return mat


def get_batches(elements1, elements2, batch_size=10000):
    assert(elements1.shape == elements2.shape)
    num_elements = elements1.shape[0]
    num_batches = math.ceil(num_elements / batch_size)
    start_index = 0
    end_index = min(batch_size, num_elements)
    for i in range(num_batches):
        start_index = i * batch_size
        end_index = min(start_index + batch_size, num_elements)
        yield (
            elements1[start_index:end_index].toarray(),
            elements2[start_index:end_index].toarray()
        )

    start_index = min(start_index + batch_size, num_elements - 1)
    end_index = num_elements

    if start_index == num_elements - 1:
        return
    yield elements1[start_index:end_index].toarray(), elements2[start_index:end_index].toarray()
