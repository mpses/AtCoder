#!/usr/bin/env pypy
n = int(input())
F = [1] * -~n
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        F[j] += 1
print(sum(e * v for e, v in enumerate(F)))