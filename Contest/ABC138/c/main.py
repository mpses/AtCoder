#!/usr/bin/env python3
_ = input()
_v, *v = sorted(map(int, input().split()))
for i in v:
    _v = (_v + i) / 2
print(_v)