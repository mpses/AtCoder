#!/usr/bin/env python3
import numpy as np
b = abs
n, *a = map(int, open(0).read().split())
a = np.array([0] + a + [0])
s = sum(map(b, a[1:] - a[:-1]))
for i in range(n):
    print(s + b(a[i+2] - a[i]) - b(a[i+1] - a[i]) - b(a[i+2] - a[i+1]))