#!/usr/bin/env python3
class UnionFind():
    def __init__(self, n):
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

(n, m), a, *q = [[*map(int,o.split())] for o in open(0)]
UF = UnionFind(n)
k = (n - m - 1) * 2
if k > n:
    exit(print("Impossible"))
if not k:
    exit(print(0))

for c, f in q:
    UF.union(c, f)

from collections import*
d = defaultdict(list)
for e, i in enumerate(a):
    d[UF.find(e)] += i,

ans, b = 0, []
for r, p in d.items():
    p.sort()
    ans += p.pop(0)
    b += p
    k -= 1
b.sort()
print(ans + sum(b[:k]))