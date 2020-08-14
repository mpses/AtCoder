#!/usr/bin/env python3
import re
print("YES" if re.fullmatch("(eraser?|dream(er)?)+", input()) else "NO")