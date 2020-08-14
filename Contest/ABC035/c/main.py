#!/usr/bin/env python3
from itertools import*
class Imos:
    def __init__(self, n):
        self.B = [0] * n
        self.n = n

    def __call__(self, l, r, v = 1):
        l, r = max(l, 0), min(r, self.n - 1)
        self.B[l] += v
        if r + 1 != self.n:
            self.B[r + 1] -= v

    def out(self):
        *res, = accumulate(self.B)
        # self.__init__(self.n)
        return res

(n, q), *Q = [[*map(int, o.split())] for o in open(0)]
imos = Imos(n + 1)
for l, r in Q:
    imos(l, r)
print(*[i%2 for i in imos.out()[1:]], sep = "")