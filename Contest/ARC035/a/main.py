#!/usr/bin/env python3
import re
s = input()
print("YES" if all(a == b or "*" in (a, b) for a, b in zip(s, s[::-1])) else "NO")