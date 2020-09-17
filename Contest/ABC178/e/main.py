#!/usr/bin/env python3
(n,), *d = [[*map(int, o.split())] for o in open(0)]
M = [[x - y for x, y in d], [x + y for x, y in d]]
print(max(max(M[d]) - min(M[d]) for d in [0, 1]))