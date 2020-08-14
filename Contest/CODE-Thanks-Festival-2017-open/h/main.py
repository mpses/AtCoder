#!/usr/bin/env python3
INF = 10**6

import sys
input = sys.stdin.readline

# PartiallyPersistentUnionFind
class PPUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.time = [INF] * n
        r = [None] * n
        self.number_time = [[0] for _ in r]
        self.number_dots = [[1] for _ in r]

    def find(self, x, t):
        while self.time[x] <= t:
            x = self.parents[x]
        return x
        ########### or ###########
        # if self.time[x] > t:
        #    return x
        # return self.find(self.parents[x], t)

    def union(self, x, y, t):
        x = self.find(x, t)
        y = self.find(y, t)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.number_time[x] += [t]
        self.number_dots[x] += [-self.parents[x]]
        self.time[y] = t

    def same(self, x, y, t = 0):
        if x == y:
            return t
        if self.time[x] == self.time[y] == INF:
            return -1
        if self.time[x] > self.time[y]:
            x, y = y, x
        return self.same(self.parents[x], y, self.time[x])

n, m = map(int, input().split())
UF = PPUnionFind(n + 1)
for t in range(m):
    a, b = map(int, input().split())
    UF.union(a, b, t + 1)

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(UF.same(x, y))