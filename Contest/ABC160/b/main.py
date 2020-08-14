#!/usr/bin/env python3
x = int(input())
a, b = divmod(x, 500)
print(a * 1000 + b // 5 * 5)