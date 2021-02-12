#!/usr/bin/env python3
(n, s, d), *z = [[*map(int, o.split())] for o in open(0)]
print("Yes" if any(x < s and y > d for x, y in z) else "No")