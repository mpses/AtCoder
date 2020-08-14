#!/usr/bin/env python3
from numpy import*
w, n, k, *c = map(int, open(0).read().split())
dp = array([[0]*-~k for _ in [0]*-~w])
for a, b in zip(c[::2], c[1::2]):
    dp[a:,1:] = maximum(dp[:-a,:-1]+b, dp[a:,1:])
print(dp.max())