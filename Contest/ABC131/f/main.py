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

(n,), *q = [[*map(int,o.split())] for o in open(0)]
MAX = 10 ** 5 + 1
UF = UnionFind(2 * MAX)
for x, y in q:
    UF.union(x, y + MAX)
cnt_x = [0] * (2 * MAX)
cnt_y = cnt_x[:]
for i in range(MAX):
    cnt_x[UF.find(i)] += 1
    cnt_y[UF.find(i + MAX)] += 1
print(sum(X * Y for X, Y in zip(cnt_x, cnt_y)) - n)