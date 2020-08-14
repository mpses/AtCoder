#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = [i%4 for i in a]
f, t = s.count(0), s.count(2)
print("YNeos"[n-f-t+(t>0) > f+1::2])