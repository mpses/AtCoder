#!/usr/bin/env python3
from itertools import*
s = input()
if 3 >= len(s):
    for j in permutations(s):
        if int("".join(j)) % 8 == 0:
            print("Yes")
            exit()
    else:
        print("No")
        exit()
C = [0] * 10
for i in s:
    i = int(i)
    C[i] = min(3, C[i] + 1)
P = []
for e, c in enumerate(C):
    P += [e] * c
for i in permutations(P, 3):
    if int("".join(map(str,i))) % 8 == 0:
        print("Yes")
        exit()
print("No")