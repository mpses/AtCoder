#!/usr/bin/env python3
n, *a = map(int, open(0))
print(-(-n // min(a)) + 4)