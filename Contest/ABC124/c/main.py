#!/usr/bin/env python3
s = input()
a = int(("10" * 10**5)[:len(s)], 2)
s = int(s, 2)
c = lambda x: str(bin(x^s)).count("1")
print(min(c(a), c(a>>1)))