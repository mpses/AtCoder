#!/usr/bin/env python3
from collections import*
a = input()
j = lambda x: x*~-x//2
print(j(len(a)) - sum(map(j, Counter(a).values())) + 1)