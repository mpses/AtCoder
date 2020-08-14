#!/usr/bin/env python3
(n, d, k), *D = [[*map(int, o.split())] for o in open(0)]
for s, t in D[d:]:
    A = s < t
    for e, (l, r) in enumerate(D[:d], 1):
        if l <= s <= r:
            s = [l, r][A]
        if [s <= t, t <= s][A]:
            print(e)
            break