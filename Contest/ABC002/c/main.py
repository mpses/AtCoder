#!/usr/bin/env python3
A, a, B, b, C, c = map(int, input().split())
a, b, c, d = B - A, b - a, C - A, c - a
print(abs(a*d - b*c)/2)