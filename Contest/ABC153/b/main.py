#!/usr/bin/env python3
h, _, *a = map(int, open(0).read().split())
print("Yes" if sum(a) >= h else "No")