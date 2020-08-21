#!/usr/bin/env python3
a, b = map(int, open(0))
ans, MOD = 0, 10**9 + 7
for i in range(a, b + 1):
    ans = (ans + -~i * i * i // 2) % MOD
print(ans)