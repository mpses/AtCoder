#!/usr/bin/env python3
def LIS(A: list):
    from bisect import bisect_left
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            # Lの末尾よりaが大きければ増加部分列を延長できる
            L += a,
        else:
            # そうでなければ、「aより小さい最大要素の次」をaにする
            # 該当位置は二分探索で特定できる
            L[bisect_left(L, a)] = a
    return len(L)

n, *c = map(int, open(0))
print(n - LIS(c))