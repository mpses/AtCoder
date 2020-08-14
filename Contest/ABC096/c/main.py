#!/usr/bin/env python3
h, w = map(int, input().split())
b = ".";j = [b+b*w+b]
s = j + [b+input()+b for _ in [0]*h] + j
for i in range(1, h+1):
    d = [n+1 for n in range(w) if s[i][n:n+3] == ".#."]
    if d and any([s[i-1][c] == s[i+1][c] == b for c in d]):
        print("No");exit()
print("Yes")