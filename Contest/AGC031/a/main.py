#!/usr/bin/env python3
from collections import*
MOD = 10**9+7
input();i = 1
for c in Counter(input()).values():i *= c+1
print(~-i % MOD)