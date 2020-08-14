#!/usr/bin/env python3
def f(n):
    return 3*n + 1 if n%2 else n // 2

l = [int(input())]
c = 2

while True:
    i = f(l[c-2])
    if i in l:
        print(c)
        exit()
    l += [i]
    c += 1