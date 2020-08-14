#!/usr/bin/env python3
h = [0 < i%7 < 6 for i in range(366)]  # 平日
t = [31, 29, 31] + [30, 31]*2 + [31, 30]*2  # 月の日数リスト
for _ in range(int(input())):
    m, d = map(int, input().split("/"))
    d = sum(t[:m-1]) + d - 1
    while d<365 and h[d]<1:
        d += 1
    h[d] = 0
m = c = 0
for d in h:
    c += 1
    if d:
        m = max(m, c-1)
        c = 0
print(max(m, c))