#!/usr/bin/env python3
s = input()
l = len(s)
for i in range(l):
    c = s + "#" * i
    j = 1
    while j <= (l + i) // 2:
        if c[j - 1] != c[-j] != "#":
            break
        j += 1
    else:
        print(i)
        exit()