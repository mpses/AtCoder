#!/usr/bin/env python3
from string import*
from itertools import*
b = ascii_lowercase
s = input()
l = len(s)
if len(s) < 26:
    print(s + sorted(set(b) - set(s))[0])
else:
    a = [p*len(list(k)) for p, k in groupby([i < j for i, j in zip(s[::-1], s[-2::-1])])][0]
    d = - a[0]*a[1] - 2
    print(-(d < -26) or s[:d] + sorted(set(s[d+1:]) - set(b[:ord(s[d]) - 97]))[0])