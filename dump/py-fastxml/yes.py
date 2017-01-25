import scipy.sparse as sp

n_feats = 10
feats = [0,9]
vals = [1,4]
a = sp.csr_matrix((vals, ([0] * len(vals), feats)), shape=(1, n_feats), dtype='float32')
print(a.todense())