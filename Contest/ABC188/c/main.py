#!/usr/bin/env python3
def separate(a: list, length) -> zip:
    return zip(*[iter(a)] * length)

n, *a = map(int, open(0).read().split())
b = a[:]
for _ in [0] * (n - 1):
    a = [*map(max, separate(a, 2))]
print(b.index(min(a)) + 1)