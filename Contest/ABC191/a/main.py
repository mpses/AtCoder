#!/usr/bin/env python3
v, t, s, d = map(int, input().split())
print("No" if v * t <= d <= v * s else "Yes")