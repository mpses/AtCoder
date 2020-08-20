#!/usr/bin/env python3
*t, = map(int, open(0).read().split())
try:
    m = 10 - min([i%10 for i in t if i%10])
except ValueError:
    m = 0
print(sum([-(-j // 10) for j in t])*10 - m)