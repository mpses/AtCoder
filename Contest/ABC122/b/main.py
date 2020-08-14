#!/usr/bin/env python3
import re
print(max(map(len, re.findall("[ACGT]*", input()))))