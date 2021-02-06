#!/usr/bin/env python3
(n,), *z = [[*map(int, o.split())] for o in open(0)]
X, C = 0, []
for a, b in z:
    X -= a
    C += a * 2 + b,
C.sort()
ans = 0
while X <= 0:
    X += C.pop()
    ans += 1
print(ans)