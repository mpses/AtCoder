#!/usr/bin/env python3
from collections import*
_, *a = map(int, open(0).read().split())
print(sum(v - i if i < v else v if i > v else 0 for i, v in Counter(a).items()))