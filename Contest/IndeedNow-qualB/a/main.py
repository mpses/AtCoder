#!/usr/bin/env python3
a, b, c, d = map(int, open(0).read().split())
print(abs(a-c) + abs(b-d) + 1)