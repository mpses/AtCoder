#!/usr/bin/env python3
from itertools import*
from collections import*
_, *A = map(int, open(0).read().split())
*A, = accumulate(A)
print(sum(j*~-j//2 for j in Counter([0] + A).values()))