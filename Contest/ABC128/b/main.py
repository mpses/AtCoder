#!/usr/bin/env python3
n = int(input())
s = [input().split() for i in range(n)]
print(*[i + 1 for i, _ in sorted(enumerate(s), key = lambda x: (x[1][0], -int(x[1][1])))], sep="\n")