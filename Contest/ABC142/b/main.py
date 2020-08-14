#!/usr/bin/env python3
_, k, *h = map(int, open(0).read().split())
print(sum(i >= k for i in h))