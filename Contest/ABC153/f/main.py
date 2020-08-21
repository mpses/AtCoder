#!/usr/bin/env python3
class Bit2:
    def __init__(self, n):
        self.bit0 = Bit(n)
        self.bit1 = Bit(n)

    def add(self, l, r, x):
        # [l, r) に x を足す
        self.bit0.add(l, -x * (l - 1))
        self.bit1.add(l, x)
        self.bit0.add(r, x * (r - 1))
        self.bit1.add(r, -x)

    def sum(self, l, r):
        res = 0
        res += self.bit0.sum(r) + self.bit1.sum(r) * (r - 1)
        res -= self.bit0.sum(l) + self.bit1.sum(l) * (l - 1)
        return res

(n, d, a), *d = [[*map(int, o.split())] for o in open(0)]
B = Bit2(n)
for i in range(n):
    B.add(i, i + 1, )
    # solving