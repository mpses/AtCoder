#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a = [0]*3 + a
for i in range(n):
    i *= 3
    t, x, y = map(lambda j:abs(a[i+3+j]-a[i+j]), [0,1,2])
    d = x+y
    if d>t or d%2-t%2: print("No"); exit()
print("Yes")