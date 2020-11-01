#!/usr/bin/env python3
# dp[i] = Σ[s∈S] dp[i-s]
# dp[i] = Σ[s = 1 to k] Σ[t = l to r] dp[t]
# dp[i] = Σ[s = 1 to k](adp[i - r + 1] - adp[i - l])
MOD = 998244353
(n, k), *S = [[*map(int, o.split())] for o in open(0)]
dp = [0] * -~n
dp[0] = 1
adp = [0] + [1] * n # 累積和
for i in range(1, n):
    for l, r in S:
        dp[i] += (adp[max(i - l + 1, 0)] - adp[max(i - r, 0)]) % MOD
        adp[i + 1] = adp[i] + dp[i]
print(dp[n - 1] % MOD)