#!/usr/bin/env python3
n, a, b = map(int, input().split())
q, mod = divmod(n, (a+b))
if mod > a:
    mod = a
print(q*a + mod)