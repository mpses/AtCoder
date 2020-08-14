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

def I(t: "hhmm") -> "min.":
    h, m = map(int, (t[:2], t[2:]))
    return h * 60 + m

def O(t: "min.") -> "hhmm":
    h, m = divmod(t, 60)
    return str(h).zfill(2) + str(m).zfill(2)

def round5(a, b):
    return a // 5 * 5, 0--b // 5 * 5

imos = Imos(24 * 60 + 1)
for i in range(int(input())):
    imos(*round5(*map(I, input().split("-"))))

D = imos.out()
S = [[*l] for k, l in groupby(range(24 * 60 + 1), key = lambda i: D[i] > 0) if k]
for s, *_, e in S:
    print(f"{O(s)}-{O(e)}")