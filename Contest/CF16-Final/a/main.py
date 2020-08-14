#!/usr/bin/env python3
from string import*
h, w, *s = open(0).read().split()
a, b = divmod(s.index("snuke"), int(w))
print(ascii_uppercase[b] + str(a+1))