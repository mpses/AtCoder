#!/usr/bin/env python3
n = int(input())
MOD = 10**9+7
print((pow(10, n, MOD) - pow(9, n, MOD) * 2 + pow(8, n, MOD)) % MOD)