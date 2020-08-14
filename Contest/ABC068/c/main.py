#!/usr/bin/env python3
n, m = map(int, input().split())
c = {tuple(map(int, input().split())) for _ in [None]*m}
for i in range(2, n):
    if {(1, i), (i, n)} <= c:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
