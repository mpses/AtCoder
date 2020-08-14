#!/usr/bin/env python3
def t(): return range(int(input())+1)

from itertools import product as p

a = 0
s = p(t(),t(),t())
x = int(input())

for i, j, k in s:
    if i*500 + j*100 + k*50 == x:
        a += 1
print(a)