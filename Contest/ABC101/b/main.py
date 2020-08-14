#!/usr/bin/env python3
n = input()
print("YNeos"[int(n)%sum(map(int, n))>0::2])