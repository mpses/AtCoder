#!/usr/bin/env python3

def meg_bisect(ng, ok, func):
    # 二分探索・二分法 O(logn)
    # 半開区間 (ng, ok] / [ok, ng)
    # func: 単調増加関数
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

f = lambda k: sum(a * (k ** r) for r, a in x) <= m
x = input()
y = int(x)
*x, = map(int, x[::-1])
m = int(input())
d = max(x) + 1
*x, = enumerate(x)

if len(x) == 1:
    if y <= m: print(1)
    else: print(0)
    exit()

if not f(d):
    print(0)
    exit()

print(meg_bisect(10 ** 36, d, f) - d + 1)