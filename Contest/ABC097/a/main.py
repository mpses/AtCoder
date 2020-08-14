#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
print("No" if min(abs(a-c), max(abs(a-b), abs(b-c))) > d else "Yes")