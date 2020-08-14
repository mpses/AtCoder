#!/usr/bin/env python3
n, k, s = map(int, input().split())
print(*[s]*k + [(s+1)%10**9]*(n-k))