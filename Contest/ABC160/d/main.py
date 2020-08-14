#!/usr/bin/env python3
n, x, y = map(int, input().split())
a = abs
d = [0] * n
for i in range(1, n+1):
    for j in range(i + 1, n+1):
        d[min(j-i, a(x-i)+a(y-j)+1, a(x-j)+a(y-i)+1)] += 1
print(*d[1:], sep="\n")