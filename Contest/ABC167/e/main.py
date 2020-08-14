#!/usr/bin/env python3
class Factorial:
    def __init__(self, n, mod):
        self.f = f =[0] * (n + 1)
        f[0] = b = 1
        for i in range(1, n + 1):f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[n] = b = pow(self.f[n], -1, mod)
        for i in range(n,0,-1):inv[i-1] = b = b * i % mod
        self.mod = mod
    def factorial(self, i):
        return self.f[i]
    def ifactorial(self, i):
        return self.inv[i]
    def comb(self, n, k):
        if n >= k:return self.f[n] * self.inv[n - k] * self.inv[k] % self.mod
        else:return 0

MOD = 998244353
nCr = Factorial(5*10**5, MOD).comb
N, M, k = map(int, input().split())
print(sum(nCr(N - 1, x) * M * pow(M - 1, N - x - 1, MOD) % MOD for x in range(-~k)) % MOD)