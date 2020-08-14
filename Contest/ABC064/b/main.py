#!/usr/bin/env python3
_, *l = map(int, open(0).read().split())
print(max(l)-min(l))