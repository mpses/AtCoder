#!/usr/bin/env python3
s = input()
o, e = s[::2], s[1::2]
print("Yes" if o.lower() == o and e.upper() == e else "No")