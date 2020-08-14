#!/usr/bin/env python3
s, k, t = input(), int(input()), ""
for s in s:
    if (p := 123 - ord(s)) <= k:
        k -= p
        t += "a"
    else:
        t += s
k %= 26
print(t[:-1] + chr((ord(t[-1]) - 97 + k) % 26 + 97))