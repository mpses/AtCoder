#!/usr/bin/env python3
p, *q = open(0)
h, w, k = map(int, p.split())
s = [list(i.strip()) for i in q]
c = 1
r = range
for y in r(h):
    # 番号
    for x in r(w):
        if s[y][x] == "#":
            s[y][x] = c
            c += 1
        else:
            s[y][x] = 0
    # 左から右
    for x in r(w):
        if s[y][x] == 0 and x:
            s[y][x] = s[y][x - 1]
    # 右から左
    for x in r(w):
        if s[y][-x-1] == 0 and x:
            s[y][-x-1] = s[y][-x]
for x in r(w):
    # 上から下
    for y in r(h):
        if s[y][x] == 0 and y:
            s[y][x] = s[y - 1][x]
    # 下から上
    for y in r(h):
        if s[-y-1][x] == 0 and y:
            s[-y-1][x] = s[-y][x]
for i in s:
    print(*i)