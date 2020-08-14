#!/usr/bin/env python3
import re
s = input()
print("Yes" if re.fullmatch("[RUD]*", s[::2]) and re.fullmatch("[LUD]*", s[1::2]) else "No")