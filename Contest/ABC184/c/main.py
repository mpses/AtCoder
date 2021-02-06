#!/usr/bin/env python3
sx, sy, gx, gy = map(int, open(0).read().split())
r, c = gx - sx, gy - sy

if r == c == 0:
    print(0)
elif r in (c, -c) or abs(r) + abs(c) <= 3:
    print(1)
elif (r - c) % 2 == 0:
    print(2)
elif abs(r) + abs(c) <= 6:
    print(2)
elif abs(r + c) <= 3:
    print(2)
elif abs(r - c) <= 3:
    print(2)
else:
    print(3)