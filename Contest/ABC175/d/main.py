#!/usr/bin/env python3
(n, k), p, c = [[*map(int,o.split())] for o in open(0)]

p = [i - 1 for i in p]
best = max(c)

"""
for i in range(n):
    cnt, score, start = 0, [0], i
    while p[start] != i:
        start = p[start]
        cnt += c[start]
        score += cnt,
    cscore, clen = score[-1] + c[i], len(score)

    for j in range(clen):
        if j <= k and j:
            (k - j) // clen
"""