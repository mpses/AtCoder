#!/usr/bin/env python3
from math import factorial as f
C = lambda n, r: f(n) // (f(n - r) * f(r))
print(C(int(input()) - 1, 11))