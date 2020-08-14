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


(n, m), *D = [[*map(int, o.split())] for o in open(0)]
imos = Imos(m + 1)
for k in D:
    imos(*k)
print(sum(d[2] for d in D) - min(imos.out()[1:]))