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

n = int(input())
if n <= 2:
    print(1)
    exit()
# 1, 2, 3, ... k を n + 1 からまず切り取るのが最適
t = meg_bisect(0, n, lambda k: k * (k + 1) // 2 > n + 1)
print(n - t + 2)