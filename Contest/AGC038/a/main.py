#!/usr/bin/env python3
import numpy as np
*s, a, b = map(int, input().split())
p = np.ones(s, dtype=np.int)
p[:b,:a] = 0
p[b:,a:] = 0
print("\n".join("".join(q) for q in p.astype(str)))