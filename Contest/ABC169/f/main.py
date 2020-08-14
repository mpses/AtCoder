#!/usr/bin/env python3
import numpy as np
_, s, *a = map(int, open(0).read().split())
MOD = 998244353
dp = np.zeros(3100, np.int64)
dp[0] = 1
for a in a:
    g = dp.copy()
    dp[a:] += g[:-a]
    dp += g
    dp %= MOD
print(dp[s])