#!/usr/bin/env python3
INF = 10**9
from bisect import*
class PPUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.time = [INF] * n
        self.number_time = [[0] for _ in [None] * n]
        self.number_dots = [[1] for _ in [None] * n]

    def find(self, x, t):
        while self.time[x] <= t:
            x = self.parents[x]
        return x

    def union(self, x, y, t):
        x = self.find(x, t)
        y = self.find(y, t)
        if x == y:
            return 0
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.number_time[x] += [t]
        self.number_dots[x] += [-self.parents[x]]
        self.time[y] = t
        return t

    def size(self, x, t):
        x = self.find(x, t)
        return self.number_dots[x][bisect_left(self.number_time[x], t) - 1]

    def whensame(self, x, y, t = 0):
        if x == y:
            return t
        if self.time[x] == self.time[y] == INF:
            return -1
        if self.time[x] > self.time[y]:
            x, y = y, x
        return self.whensame(self.parents[x], y, self.time[x])

    def same(x, y, t):
        return self.find(x, t) == self.find(y, t)

(n, m), *q = [[*map(int, o.split())] for o in open(0)]
UF = PPUnionFind(n + 1)
for t, (a, b) in enumerate(q[:m], 1):
    UF.union(a, b, t)

for x, y in q[m + 1:]:
    print(UF.whensame(x, y))