#!/usr/bin/env python3
a, b = input().split()
print(["<>"[a > b], "="][a == b])