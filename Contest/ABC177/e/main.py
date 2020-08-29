#!/usr/bin/env python3
class Osa_k:
    def __init__(self, n_max):
        self.n_max = n_max
        self.min_factor = min_factor = list(range(n_max + 1))
        min_factor[2::2] = [2] * (n_max // 2)
        min_factor[3::6] = [3] * ((n_max + 3) // 6)
        for i in range(5, int(n_max ** .5) + 1, 2):
            if min_factor[i] == i:
                for j in range(i*i, n_max + 1, i):
                    if min_factor[j] == j:
                        min_factor[j] = i

    def __call__(self, n):
        if not 1 <= n <= self.n_max: raise ValueError("Invaild Value!")
        min_factor = self.min_factor
        n_twoes = (n & -n).bit_length() - 1
        res = [2] * n_twoes
        n >>= n_twoes
        resappend = res.append
        while n > 1:
            p = min_factor[n]
            resappend(p)
            n //= p
        return set(res)

from math import gcd
_, *a = map(int, open(0).read().split())
D = set()
t = 0
k = True
fac = Osa_k(max(a))
for b in a:
    s = fac(b)
    if D & s: k = False
    D |= s
    t = gcd(t, b) if t else b
if k:
    print("pairwise coprime")
elif t == 1:
    print("setwise coprime")
else:
    print("not coprime")