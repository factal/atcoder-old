import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

n, m = map(int, input().split())
a = 0
b = 0
if n >= 2:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
else:
    a = int(input())
    b = int(input())

if m >= 1:

    edge = np.array([input().split() for _ in range(m)], dtype = np.int64).T
    tmp = np.ones(m, dtype = np.int64).T
    graph = csr_matrix((tmp, (edge[:] -1)), (n, n))

    data = connected_components(graph)
    svals = [0] * data[0]
    evals = [0] * data[0]

    for i in enumerate(a):
        svals[data[1][i[0]]] += i[1]

    for i in enumerate(b):
        evals[data[1][i[0]]] += i[1]

    if svals == evals:
        print("Yes")
    else:
        print("No")

else:
    if a == b:
        print("Yes")
    else:
        print("No")