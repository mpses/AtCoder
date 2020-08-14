#!/usr/bin/env python3
n = input()
print("No" if int(n) % sum(map(int, n)) else "Yes")
