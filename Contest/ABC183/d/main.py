#!/usr/bin/env python3
from itertools import*
class Imos:
    def __init__(self, n):
        self.B = [0] * n
        self.n = n

    # warning : [l, r] or [l, r)
    def __call__(self, l, r, v = 1):
        l, r = max(l, 0), min(r, self.n - 1)
        self.B[l] += v
        if r + 1 != self.n:
            self.B[r + 1] -= v

    def out(self):
        *res, = accumulate(self.B)
        # self.__init__(self.n)
        return res

(n, w), *q = [[*map(int, o.split())] for o in open(0)]
imos = Imos(3 * 10 ** 5)
for s, t, p in q:
    imos(s, t - 1, p)
print("Yes" if max(imos.out()) <= w else "No")