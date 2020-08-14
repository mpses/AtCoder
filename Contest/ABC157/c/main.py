#!/usr/bin/env python3
n, m = map(int, input().split())
L = [list(map(int,input().split())) for _ in range(m)] #s_i, c_i
j = 0 if n == 1 else 10**(n-1)
for i in range(j,10**n):
    st = str(i)
    if all(st[s-1] == str(c) for s, c in L): #全てにおいて[s=c]すなわち[stのs番目の文字＝c]となるとき
        print(i)
        exit()
print(-1)