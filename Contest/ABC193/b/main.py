#!/usr/bin/env python3
INF = float("inf")
(n,), *z = [[*map(int, o.split())] for o in open(0)]
ans = INF
for a, p, x in z:
    if x > a:
        ans = min(ans, p)
print(ans if ans != INF else -1)