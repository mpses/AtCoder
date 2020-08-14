#!/usr/bin/env python3
l = sorted(map(int, input().split()))
for _ in range(int(input())):
    l[2] *= 2
    l.sort
print(sum(l))