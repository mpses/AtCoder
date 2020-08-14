#!/usr/bin/env python3
MOD = 998244353

class Factorial:
    def __init__(self, n, mod):
        self.f = f =[0] * (n + 1)
        f[0] = b = 1
        for i in range(1, n + 1):
            f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[n] = b = pow(self.f[n], -1, mod)
        for i in range(n, 0, -1):
            inv[i - 1] = b = b * i % mod
        self.mod = mod

    def factorial(self, i):
        return self.f[i]

    def ifactorial(self, i):
        return self.inv[i]

    def C(self, n, k):
        if not 0 <= k <= n: return 0
        return self.f[n] * self.inv[n - k] * self.inv[k] % self.mod

    def P(self, n, k):
        if not 0 <= k <= n: return 0
        return self.f[n] * self.inv[n - k] % self.mod

    def H(self, n, k):
        if (n == 0 and k > 0) or k < 0: return 0
        return self.f[n + k - 1] * self.inv[k] % self.mod * self.inv[n - 1] % self.mod


# pA + qB = K
n, a, b, k = map(int, input().split())
F = Factorial(n, MOD)
c = 0
for p in range(k // a + 1):
    q, _ = divmod(k - p*a, b)
    if _:continue
    c = (c + F.C(n, p) * F.C(n, q)) % MOD
print(c)