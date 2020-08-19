#!/usr/bin/env python3
k, x = map(int, input().split())
print(*range(x - k + 1, x + k))