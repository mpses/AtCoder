#!/usr/bin/env python3
x, y = map(int, input().split())
print("Yes" if abs(x - y) < 3 else "No")