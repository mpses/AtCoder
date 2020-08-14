#!/usr/bin/env python3
#!!!
n = int(input())

def j(b):
    print(b)
    i = input()[0]
    if i == "V": exit()
    return b, i

def q(l, r, t):
    m, rm = j((l + r + 1) // 2)
    if (m - b)%2 == (rm != t):
        q(m, r, rm)
    else:
        q(l, m-1, t)

_, s = j(0)
q(0, n-1, s)