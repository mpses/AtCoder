#!/usr/bin/env python3
_, k, *l = map(int, open(0).read().split())
for a,b in sorted(zip(*[iter(l)]*2)):
 k -= b
 if k < 1:print(a);exit()