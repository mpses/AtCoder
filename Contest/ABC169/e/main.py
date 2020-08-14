#!/usr/bin/env python3
import numpy as np
(n,), *d = [[*map(int, i.split())] for i in open(0)]
a, b = np.median(d, axis=0)
if n%2:print(int(b - a + 1))
else:print(int(b*2 - a*2 + 1))