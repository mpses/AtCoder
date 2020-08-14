#!/usr/bin/env python3
d = [list(map(int, input().split())) for _ in [0]*int(input())]
print(sum(sorted(sum(c) for c in d)[::-2]) - sum(c[1] for c in d))