#!/usr/bin/env python3
x, k, d = map(int, input().split())
if x < 0:
    a, b = divmod(-x, d)
    if a >= k:
        print(-x - k * d);exit()
    else:
        print(d - b if (k - a) % 2 else b)
elif x:
    a, b = divmod(x, d)
    if a >= k:
        print(x - k * d);exit()
    else:
        print(d - b if (k - a) % 2 else b)
else:
    print(k % 2 * d)