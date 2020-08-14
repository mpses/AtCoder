#!/usr/bin/env python3
_ = input()
*l, m = sorted(map(int, input().split()))
print("Yes" if sum(l) > m else "No")