#!/usr/bin/env python3
n, k, *a = map(int, open(0).read().split())
MOD = 10**9+7
M = len([i for i in a if i < 0])
a.sort()
ans, c = 1, 0
while c < min(M//2, k//2):
    A, B = a.pop(0), a.pop(0)
    ans = ans * -A #% MOD
    ans = ans * -B #% MOD
    c += 1
for i in a[::-1][:(k-c*2)]:
    ans = ans * i #% MOD
print(ans)