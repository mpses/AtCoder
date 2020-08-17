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

import string
# print(ord("A")) -> 65
code = lambda char: ord(char) - 55 if char.isalpha() else int(char)

n = int(input())
*s1, = map(code, input())
*s2, = map(code, input())

UF = UnionFind(36)
for s, t in zip(s1, s2):
    UF.union(s, t)

ans = 1
used = [False] * 36
for e, s in enumerate(s1):
    if not any(UF.same(i, s) for i in range(10)) and not used[UF.find(s)]:
        used[UF.find(s)] = True
        if e == 0:
            ans *= 9
        else:
            ans *= 10
print(ans)