#!/usr/bin/env python3
n, *w = map(int, open(0).read().split())
print(min(abs(sum(w[:i]) - sum(w[i:])) for i in range(n)))