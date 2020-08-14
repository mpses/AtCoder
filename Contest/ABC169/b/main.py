#!/usr/bin/env python3
_, *a = map(int, open(0).read().split())
a.sort()
m = 1
for i in a:
    if i > 10**18 and a[0]:
        exit(print(-1))
    m *= i
    if m > 10**18:
        exit(print(-1))
print(m)