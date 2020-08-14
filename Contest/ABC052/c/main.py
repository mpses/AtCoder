#!/usr/bin/env python3.4.3
n = int(input())
fct = {}  # prime factor
for n in range(1, n + 1):
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            fct[b] = fct.get(b, 0) + e
        b, e = b + 1, 0
    if n > 1:
        fct[n] = fct.get(n, 0) + 1
p = 1
MOD = 10**9+7
for i in fct.values():
    p *= i + 1 % MOD
    p %= MOD
print(p)