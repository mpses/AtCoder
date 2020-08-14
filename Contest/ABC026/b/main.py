#!/usr/bin/env python3
from math import pi
def s(l): 
    return sum(x*x for x in l) 
n, *t = map(int, open(0))
t.sort()
print((s(t[::-2]) - s(t[-2::-2]))*pi)