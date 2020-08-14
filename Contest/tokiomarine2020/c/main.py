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

n, k, *A = map(int, open(0).read().split())
for _ in [0] * min(k, 41):
    B = Imos(n)
    for i, a in enumerate(A):
        B(i - a, i + a)
    A = B.out()
print(*A)