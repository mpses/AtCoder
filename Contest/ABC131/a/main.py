#!/usr/bin/env python3
from itertools import groupby
print("Bad" if len(list(groupby(input()))) < 4 else "Good")