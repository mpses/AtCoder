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

def compress(a: list) -> list:
    s = sorted(set(a))
    d = {v : i for i, v in enumerate(s)}
    return s, d
    #return [d[i] for i in a]

def separate(a: list, length) -> zip:
    return zip(*[iter(lst)]*length)

(n, C), *q = [[*map(int, o.split())] for o in open(0)]
s, d = compress(sum([*zip(*q)][:2], ()))
s += s[-1] + 1,
imos = Imos(len(d))
for a, b, c in q:
    imos(d[a], d[b], c)
    ans = 0
print(imos.out())
for e, i in enumerate(imos.out()):
    ans += (s[e + 1] - s[e]) * min(C, i)
print(ans)