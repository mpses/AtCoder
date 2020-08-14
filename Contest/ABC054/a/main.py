#!/usr/bin/env python3
a, b = map(int, input().split())
print([["Alice", "Bob"][(a - 2)%13 < (b - 2)%13], "Draw"][a==b])