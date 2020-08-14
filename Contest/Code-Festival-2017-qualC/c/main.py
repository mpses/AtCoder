#!/usr/bin/env python3
s = input()
l, r = 0, len(s) - 1
c = 0
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == "x":
        l += 1
        c += 1
    elif s[r] == "x":
        r -= 1
        c += 1
    else:
        print(-1)
        exit()
print(c)