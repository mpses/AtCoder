#!/usr/bin/env python3
_, *a = map(int, open(0).read().split())
print(*[i for i, _ in sorted(enumerate(a, 1), key = lambda l: l[1])])