#!/usr/bin/env python3
a, b, c = sorted(map(int, input().split()))
d = b - a
print(c - b + d//2 + d%2cc *2)