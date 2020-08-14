#!/usr/bin/env python3
n = input()
print(10 if len(set(n)) == 2 and n[:2] == "10" else sum(map(int, n)))