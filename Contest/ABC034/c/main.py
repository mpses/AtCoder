#!/usr/bin/env python3
w, h = map(int, input().split())
w -= 1
h -= 1

# 逆元計算 (3.8からはpowerがpowでできるので 3.8より前)
def modinv(a, mod):
    return pow(a, mod - 2, mod)

# pow Ver別
def power(a, b, c = None):
    try:
        return pow(a, b, c)
    except (ValueError, TypeError) as e:
        if b < 0:
            return pow(modinv(a, c), -b, c)
        else:
            print(e)
            return

class Factorial:
    def __init__(self, n, mod):
        self.f = f =[0] * (n + 1)
        f[0] = b = 1
        for i in range(1, n + 1):
            f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[n] = b = power(self.f[n], -1, mod)
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

INF = 10**6
MOD = 10**9+7

def nCr(n, r, mod = MOD, limit = INF):
    return Factorial(limit, mod).C(n, r)

print(nCr(w + h, w))