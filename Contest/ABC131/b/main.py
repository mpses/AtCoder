#!/usr/bin/env python3
n, l = map(int, input().split())
t = list(range(l, l + n))
s = [abs(_) for _ in t]
print(sum(t) - t[s.index(min(s))])