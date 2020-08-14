#!/usr/bin/env python3
x, a, b = map(int, input().split())
print(["delicious", ["safe", "dangerous"][b-a>x]][b-a>0])