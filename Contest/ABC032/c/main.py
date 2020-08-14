#!/usr/bin/env python3
N, K, *a = map(int, open(0).read().split())
if 0 in a:
    exit(print(N))
if K == 0:
    exit(print(0))
left, total, ans = 0, 1, 0
for right in range(N):
    total *= a[right]
    while total > K:
        total //= a[left]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)