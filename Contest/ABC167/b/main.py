#!/usr/bin/env python3
a, b, c, k = map(int, input().split())
i = min(a, k)
k -= i
k -= min(b, k)
print(i-k)