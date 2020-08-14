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

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

UF = UnionFind(n + 1)

F = 1
for _ in [0] * m:
    a, b, y = map(int, input().split())
    data += [-y, F, a, b],

q = int(input())

F = 0
for i in range(q):
    v, w = map(int, input().split())
    data += [-w, F, i, v],


# 1. based on weight ; 大きい方を前に来るようにソートするのでマイナス
# 2. based on F ; 先に質問に答える (F = 0)
data.sort()

ans = [0] * q
for _, F, c, d in data:
    if F:
        UF.union(c, d)
    else:
        ans[c] = UF.size(d)

for s in ans:
    print(s)
