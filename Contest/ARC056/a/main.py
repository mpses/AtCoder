#!/usr/bin/env python3
a, b, k, l = map(int, input().split())
c, d = divmod(k, l)
print(b*c + min(b, a*d))