#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, q = map(int, input().split())

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

UF = UnionFind(n*2)
for _ in [None]*q:
    w, x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if w == 1:
        if z%2:
            UF.union(x, y + n)
            UF.union(y, x + n)
        else:
            UF.union(x, y)
            UF.union(x + n, y + n)
    else:
        print("YES" if UF.same(x, y) else "NO")