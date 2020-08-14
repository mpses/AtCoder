#!/usr/bin/env python3
b = 1
x = int(input())
while True:
    a = (x-a**5)**.2
    if float.is_integer(b):
        print(int(a), -b)
        exit()
    b += 1