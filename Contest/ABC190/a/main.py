#!/usr/bin/env python3
a, b, c = map(int, input().split())
print(["Aoki", "Takahashi"][a > b if a != b else c])