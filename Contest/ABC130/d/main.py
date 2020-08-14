#!/usr/bin/env python3
N, K, *a = map(int, open(0).read().split())
left, total, ans = 0, 0, 0
for right in range(N):
    total += a[right]
    while total >= K:
        ans += N - right 
        total -= a[left]
        left += 1
print(ans)