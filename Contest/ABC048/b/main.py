#!/usr/bin/env python3
a, b, x = map(int, input().split())
print(b // x - ~-a // x)