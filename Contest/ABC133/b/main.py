#!/usr/bin/env python3
n, d = map(int, input().split())

def dis(y, z):
    return (sum([(y[i] - z[i]) ** 2 for i in range(d)]) ** .5).is_integer()

l = [[int(i) for i in input().split()] for _ in range(n)]

c = 0
for p in range(n - 1):
    for q in range(p + 1, n):
        c += dis(l[p], l[q])
print(c)