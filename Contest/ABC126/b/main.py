#!/usr/bin/env python3
s = input()
F = 0 < int(s[:2]) < 13
S = 0 < int(s[2:]) < 13
print("AMBIGUOUS" if F*S else "YYMM" if S else "MMYY" if F else "NA")