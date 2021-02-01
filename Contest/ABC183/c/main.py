#!/usr/bin/env python3
(n, k), *t = [[*map(int, o.split())] for o in open(0)]
from itertools import*
ans = 0
for s in permutations(range(1, n)):
    s = [0, *s, 0]
    ans += sum(t[i][j] for i, j in zip(s, s[1:])) == k
print(ans)