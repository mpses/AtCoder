#!/usr/bin/env python3
class UnionFind():
    def __init__(self, n, m = None, read = 0):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

(n, k, l), *d = [[*map(int, o.split())] for o in open(0)]
R, T = UnionFind(n), UnionFind(n)
for p, q in d[:k]:
    R.union(p - 1, q - 1)
for r, s in d[k:]:
    T.union(r - 1, s - 1)
C = []
for i in range(n):
    C += (R.find(i), T.find(i)),
from collections import*
c = Counter(C)
print(*[c[g] for g in C])