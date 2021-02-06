#!/usr/bin/env python3
import numpy as np
_, a, b = [[*map(int, o.split())] for o in open(0)]
print("Yes" if np.inner(np.array(a), np.array(b)) == 0 else "No")