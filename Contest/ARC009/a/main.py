#!/usr/bin/env python3
(n,), *d = [[*map(int, o.split())] for o in open(0)]
print(int(sum(a * b for a, b in d) * 1.05))