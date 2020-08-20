#!/usr/bin/env python3
*l, k = map(int, open(0).read().split())
from itertools import*
print(":(" if any(abs(i) > k for i in map(lambda x: x[0]-x[1], permutations(l))) else "Yay!")