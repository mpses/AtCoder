#!/usr/bin/env python3
s = set(open(0).read().split("\n"))
for t in s:
    if "!" + t in s:
        print(t)
        exit()
print("satisfiable")