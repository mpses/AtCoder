#!/usr/bin/env python3
(n, d), *z = [[*map(int, o.split())] for o in open(0)]
d **= 2
print(sum(d >= x**2 + y**2 for x, y in z))