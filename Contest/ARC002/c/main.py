#!/usr/bin/env python3
from itertools import*
p = lambda x: product(x, repeat = 2)
_, s = open(0)
print(min(len(s.replace(g, "_").replace(h, "_")) for g, h in p(i + j for i, j in p("ABXY"))) - 1)