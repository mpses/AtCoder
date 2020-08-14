#!/usr/bin/env python3.4.3
from fractions import gcd
n = int(input())
print(n * 2 // gcd(2,n))