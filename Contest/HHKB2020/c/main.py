#!/usr/bin/env python3
from collections import defaultdict
n, *p = map(int, open(0).read().split())
d = defaultdict(lambda: 0)
ans = 0
for q in p:
    d[q] = 1
    while d[ans]:
        ans += 1
    print(ans)