#!/usr/bin/env python3
input()
from itertools import*
print(sum(len([*l]) // 3 for k, l in groupby(input()) if k == "X"))