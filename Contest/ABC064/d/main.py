#!/usr/bin/env python3
input()
s = input()
L = R = 0
for t in s:
    if t == "(":
        R += 1
    else:
        if R:
            R -= 1
        else:
            L += 1
print("("*L + s + ")"*R)