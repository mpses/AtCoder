#!/usr/bin/env python3
from collections import*
print(sum(i * (i - 1) // 2 for i in Counter("".join(sorted(input())) for _ in [0] * int(input())).values()))