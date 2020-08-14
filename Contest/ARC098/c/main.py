#!/usr/bin/env python3
from itertools import*
n, s = open(0)
w, e = [list(accumulate([0] + list(map(int, s.translate(str.maketrans("EW","01"[::a])))))) for a in [-1,1]]
print(w, e)