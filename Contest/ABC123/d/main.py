#!/usr/bin/env python3
(x, y, z, k), a, b, c = [[*map(int, o.split())] for o in open(0)]
a.sort(); b.sort(); c.sort()

h = [(-(a[-1] + b[-1] + c[-1]), -1, -1, -1)]
s = set(h)

from heapq import*
def push(i, j, k):
    global s, h
    try:
        t = (- (a[i] + b[j] + c[k]), i, j, k)
    except IndexError:
        return
    if t not in s:
        heappush(h, t)
        s |= {t}

for _ in [0] * k:
    p, i, j, k = heappop(h)
    print(-p)
    push(i, j, k - 1)
    push(i, j - 1, k)
    push(i - 1, j, k)