import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
import itertools
import math

n, k = map(int, input().split())
a = np.matrix([list(map(int, input().split())) for _ in range(n)])

if n >= 2:
    match_row = []
    match_column = []
    count_row = 1
    count_column = 1

    for index in itertools.combinations(range(n), 2):
        if np.all(a[index[0]] + a[index[1]] <= k):
            match_row.append(index)
        if np.all(a.T[index[0]] + a.T[index[1]] <= k):
            match_column.append(index)

    match_row.append([1, 1])
    match_column.append([1, 1])


    edge_row = np.array(match_row, dtype = np.int64).T
    edge_column = np.array(match_column, dtype = np.int64).T
    tmp_row = np.ones(len(match_row), dtype = np.int64).T
    tmp_column = np.ones(len(match_column), dtype = np.int64).T
    graph_row = csr_matrix((tmp_row, (edge_row[:])), (n, n))
    graph_column = csr_matrix((tmp_column, (edge_column[:])), (n, n))
    data_row = connected_components(graph_row)
    data_column = connected_components(graph_column)

    for i in range(data_row[0]):
        count_row *= math.factorial(np.count_nonzero(data_row[1] == i))
    for i in range(data_column[0]):
        count_column *= math.factorial(np.count_nonzero(data_column[1] == i))

    print(count_row * count_column % 998244353)

else:
    print(1)