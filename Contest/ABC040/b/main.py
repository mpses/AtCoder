#!/usr/bin/env python3
n = int(input())
print(min(abs(n//k - k) + n%k for k in range(1, n+1)))