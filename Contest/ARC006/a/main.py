#!/usr/bin/env python3
e = set(map(int, input().split()))
b = int(input())
l = set(map(int, input().split()))
c = len(e & l)
print(1 if c == 6 else 2 if c == 5 and b in l else 0 if c < 3 else 8 - c)