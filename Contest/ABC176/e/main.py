#!/usr/bin/env python3
from collections import*
(h, w, m), *d = [[*map(int, o.split())] for o in open(0)]
x, y = zip(*d)
a, e = Counter(x).most_common()[0]
b, f = Counter(y).most_common()[0]
C = defaultdict(lambda: 0)
D = defaultdict(lambda: 0)
for h, w in d:
    if h != a: C[w] += 1
for h, w in d:
    if w != b: D[w] += 1
C, D = Counter(C), Counter(D)
print(max(e + (C.most_common()[0][1] if C else 0), f + (D.most_common()[0][1] if D else 0)))