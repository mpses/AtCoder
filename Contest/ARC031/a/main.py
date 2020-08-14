#!/usr/bin/env python3
s = input()
print("YNEOS"[s!=s[::-1]::2])
