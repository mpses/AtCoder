#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a = [0] + a
b = [0] * -~n
for i in range(n, 0, -1):
    s = sum(b[j] for j in range(i, n + 1, i))
    if s % 2 != a[i]:
        b[i] = 1
print(sum(b))
print(*[i for i, b in enumerate(b) if b == 1])