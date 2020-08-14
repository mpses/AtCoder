#!/usr/bin/env python3
from scipy.sparse.csgraph import floyd_warshall
INF = float("inf")

h, w = map(int, input().split())
M = [input() for _ in [0]*h]
E = [[0]*h*w for _ in [0]*h*w]
D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def point(x, y):
    return w * x + y

for i in range(h):
    for j in range(w):
        if M[i][j] == ".":
            for x, y in D:
                I, J = i + x, j + y
                if w > J >= 0 <= I < h and M[I][J] == ".":
                    E[point(i, j)][point(I, J)] = 1

a = floyd_warshall(E)
print(int(a[a != INF].max()))