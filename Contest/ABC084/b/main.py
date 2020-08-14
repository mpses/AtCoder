#!/usr/bin/env python3
import re
a, b = map(int, input().split())
print("Yes" if re.search("\d{{{}}}-\d{{{}}}".format(a, b), input()) else "No")