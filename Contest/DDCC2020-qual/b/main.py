#!/usr/bin/env python3
from numpy import*
n, *a = map(int, open(0).read().split())
a = array(a)
print(int(min(abs(cumsum(a)-(sum(a)/2)))*2))