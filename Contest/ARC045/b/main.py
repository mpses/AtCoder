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

(n, m), *q = [[*map(int, o.split())] for o in open(0)]
imos = Imos(n + 2)
for s, t in q:
    imos(s, t)
*c, = accumulate([0] + [i > 1 for i in imos.out()])
ans = []
for e, (s, t) in enumerate(q, 1):
    if c[t + 1] - c[s] == t - s + 1:
        ans += e,
print(len(ans))
for i in ans:
    print(i)