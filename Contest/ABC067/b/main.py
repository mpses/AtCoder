#!/usr/bin/env python3
_, k, *l = map(int, open(0).read().split())
print(sum(sorted(l)[-k:]))