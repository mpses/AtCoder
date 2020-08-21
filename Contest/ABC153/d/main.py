#!/usr/bin/env python3
h = int(input())
m, c = 1, 0
while h:
    h //= 2
    c += m
    m *= 2
print(c)