#!/usr/bin/env python3
print(" HD"[eval(input().translate(str.maketrans("HD", "+-")).replace(" ","1*")+"1")])