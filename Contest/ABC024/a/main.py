#!/usr/bin/env python3
a, b, c, k, s, t = map(int, open(0).read().split())
print(a * s + b * t - (k <= s + t) * c * (s + t))