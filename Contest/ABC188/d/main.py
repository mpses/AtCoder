#!/usr/bin/env python3
def compress(a: list):
    # 座標圧縮
    s = sorted(set(a))
    d = {v : i for i, v in enumerate(s)}
    return s, d, [d[i] for i in a]

from bisect import*
from itertools import accumulate, chain
class Imos:
    # クエリ先読み座圧対応imos法
    # bisect, itertools.accumulate, itertools.chain.from_iterable, compress 必須
    def __init__(self, query: "[[l, r, v], ...]", rclosed = False):
        if rclosed:
            query = [[l, r + 1, v] for l, r, v in query]
        *code, = chain.from_iterable(query)
        self.s, code, _ = compress(code[::2] + code[1::2])
        n = len(code)
        B = [0] * n

        for l, r, v in query:
            B[code[l]] += v
            if code[r] != n:
                B[code[r]] -= v
        self.code = code
        *self.res, = accumulate(B)

    def get(self, x):
        return self.res[bisect(self.s, x) - 1]
 
    def sum(self, l, r):
        # Σ[l, r) O(n)
        s, res = self.s, self.res
        L, R = bisect(s, l) - 1, bisect(s, r) - 1
        ans = (s[L + 1] - l) * res[L]
        for i in range(L + 1, R):
            ans += (s[i + 1] - s[i]) * res[i]
        ans += (r - s[R]) * res[R]
        return ans
 
    def sumall(self):
        return self.sum(0, self.s[-1] + 1)

(_, C), *q = [[*map(int, o.split())] for o in open(0)]
imos = Imos(q, rclosed = True)
imos.res = [min(x, C) for x in imos.res]
print(imos.sumall())