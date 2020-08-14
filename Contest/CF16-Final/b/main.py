#!/usr/bin/env python3
n = int(input())
c = a = 0
while a < n:
    c += 1
    a = -~c*c//2
for i in range(1, c+1):
    if i != a - n:
        print(i)