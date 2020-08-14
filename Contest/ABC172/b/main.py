#!/usr/bin/env python3
print(len([1 for s, t in zip(input(), input()) if s != t]))