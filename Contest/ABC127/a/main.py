#!/usr/bin/env python3
a, b = map(int, input().split())
print(b if a > 12 else b // 2 if 13 > a > 5 else 0)