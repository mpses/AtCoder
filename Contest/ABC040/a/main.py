#!/usr/bin/env python3
n, x = map(int, input().split())
print(min(n-x, x-1))