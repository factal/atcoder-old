import collections
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

n, m = map(int, input().split())

if m != 0:
    edge = np.array([input().split() for _ in range(m)], dtype = np.int64).T
    tmp = np.ones(m, dtype = np.int64).T
    graph = csr_matrix((tmp, (edge[:] -1)), (n, n))

    cnt = collections.Counter(connected_components(graph)[1])

    print(max(cnt.values()))
else:
    print('1')