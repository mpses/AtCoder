#!/usr/bin/env python3
*s, = map(int, input())
print(sum(s[-2::-2]), sum(s[::-2]))