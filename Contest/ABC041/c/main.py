#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
for i in sorted(range(1, -~n), key = lambda x: a[x-1])[::-1]:
    print(i)