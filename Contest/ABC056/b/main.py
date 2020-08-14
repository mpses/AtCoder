#!/usr/bin/env python3
w, a, b = map(int,input().split())
s = abs(a-b)
print([0, s-w][s>w])