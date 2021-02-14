#!/usr/bin/env python3
MOD = 998244353
a, b, c = [i * (i + 1) // 2 % MOD for i in map(int, input().split())]
print(a * b % MOD * c % MOD)