#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
print("No" if a <= b < c <= d or c <= d < a <= b else "Yes")