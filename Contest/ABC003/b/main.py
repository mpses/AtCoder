#!/usr/bin/env python3
k = "@atcoder"
print("You", ["will lose","can win"][all(s == t or (s == "@" and t in k) or (t == "@" and s in k) for s, t in zip(input(), input()))])