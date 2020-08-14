#!/usr/bin/env python3
a, b = sorted(map(int, input().split()))
print(max(b*2-1, a+b))