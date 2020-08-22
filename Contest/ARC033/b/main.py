#!/usr/bin/env python3
_, a, b = [set(map(int, o.split())) for o in open(0)]
print(len(a & b) / len(a | b))