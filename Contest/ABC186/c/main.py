#!/usr/bin/env python3
n = int(input())
print(sum("7" not in str(i) + oct(i) for i in range(1, n + 1)))