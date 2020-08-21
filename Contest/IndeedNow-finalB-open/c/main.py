#!/usr/bin/env python3
INF = float("inf")

n = int(input())
s = input()
*c, = map(int, input().split())


dp = [INF] * -~n
dp[0] = 0
Judge = [[False] * (n - i) for i in range(n)] # Judge[l][r] := [l, r] が回文か

for center in range(n):
    for i in range(2):
        L = R = center; R += i
        while 0 <= L <= R < n and s[L] == s[R]:
            Judge[L][R - L] = 1
            L -= 1; R += 1

for i in range(n):
    for j in range(n - i): 
        if Judge[i][j]:
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + c[j])
print(dp[-1])